from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
import time
from collections import defaultdict

class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, calls: int = 100, period: int = 60):
        super().__init__(app)
        self.calls = calls
        self.period = period
        self.clients = defaultdict(list)

    async def dispatch(self, request, call_next):
        client_ip = request.client.host
        current_time = time.time()
        
        # Clean old requests
        self.clients[client_ip] = [t for t in self.clients[client_ip] if current_time - t < self.period]
        
        if len(self.clients[client_ip]) >= self.calls:
            return JSONResponse(
                status_code=429,
                content={"message": "Too many requests. Please try again later."}
            )
            
        self.clients[client_ip].append(current_time)
        return await call_next(request)
