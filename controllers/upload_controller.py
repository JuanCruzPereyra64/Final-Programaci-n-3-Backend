import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse

router = APIRouter()

# Path to save images (Frontend public folder)
UPLOAD_DIR = os.path.join(os.getcwd(), "frontend", "public", "Imagenes producto")

@router.post("/upload")
async def upload_image(file: UploadFile = File(...), product_name: str = Form(...), index: int = Form(...)):
    try:
        # Ensure directory exists
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        
        # Get extension
        file_ext = os.path.splitext(file.filename)[1]
        
        # Sanitize product name for filename
        safe_name = "".join([c for c in product_name if c.isalnum() or c in (' ', '-', '_')]).strip()
        safe_name = safe_name.replace(" ", "_")
        
        # Create new filename: Product_Name_1.jpg
        new_filename = f"{safe_name}_{index}{file_ext}"
        
        # Create file path
        file_path = os.path.join(UPLOAD_DIR, new_filename)
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Return URL relative to public folder
        image_url = f"/Imagenes producto/{new_filename}"
        
        return JSONResponse(content={"url": image_url}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
