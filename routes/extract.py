from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse

from services.extractor import extract_text_tables_images
from utils.file_ops import save_upload_file, cleanup_file, create_temp_zip

router = APIRouter()

@router.post('/extract')
async def extract(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code= 400, detail= "Only PDF files are accepted")
    
    tmp_pdf = save_upload_file(file)
    tmp_zip = create_temp_zip()

    try:
        extract_text_tables_images(tmp_pdf, tmp_zip)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Extraction error: {e}")
    finally:
        cleanup_file(tmp_pdf)
        
    return FileResponse(
        tmp_zip, 
        media_type="application/zip", 
        filename="extracted_content.zip"
    )