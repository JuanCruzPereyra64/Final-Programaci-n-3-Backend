import time
from functools import wraps
from collections import defaultdict
from fastapi import Request, HTTPException, status

# Store request timestamps per IP for the endpoint
# Format: {ip_address: [timestamp1, timestamp2, ...]}
_order_rate_limit_store = defaultdict(list)

def order_rate_limit(func):
    """
    Decorator to limit requests to the order endpoint.
    Limits to 10 requests per minute per IP.
    """
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request = kwargs.get('request')
        
        # Try to find request in args if not in kwargs
        if not request:
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break
        
        if request:
            client_ip = request.client.host
            current_time = time.time()
            
            # Clean old requests (older than 60 seconds)
            _order_rate_limit_store[client_ip] = [
                t for t in _order_rate_limit_store[client_ip] 
                if current_time - t < 60
            ]
            
            # Check limit (10 requests per minute)
            if len(_order_rate_limit_store[client_ip]) >= 10:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Too many order requests. Please try again later."
                )
                
            # Add current request
            _order_rate_limit_store[client_ip].append(current_time)
            
        return await func(*args, **kwargs)
        
    return wrapper
