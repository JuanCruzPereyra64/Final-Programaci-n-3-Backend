import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
import cloudinary
import cloudinary.uploader

router = APIRouter()

# Configure Cloudinary
cloudinary.config( 
  cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"), 
  api_key = os.getenv("CLOUDINARY_API_KEY"), 
  api_secret = os.getenv("CLOUDINARY_API_SECRET") 
)

@router.post("/upload")
async def upload_image(file: UploadFile = File(...), product_name: str = Form(...), index: int = Form(...)):
    try:
        # Sanitize product name for filename (optional, Cloudinary handles naming but good for folder organization)
        safe_name = "".join([c for c in product_name if c.isalnum() or c in (' ', '-', '_')]).strip()
        safe_name = safe_name.replace(" ", "_")
        
        # Upload to Cloudinary
        # public_id allows us to control the filename on Cloudinary
        result = cloudinary.uploader.upload(
            file.file, 
            public_id = f"products/{safe_name}_{index}",
            overwrite = True,
            resource_type = "image"
        )
        
        # Get the secure URL from Cloudinary response
        image_url = result.get("secure_url")
        
        return JSONResponse(content={"url": image_url}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
