import tempfile
import os

def save_upload_file(upload_file) -> str:
    """Save uploaded file to a temporary path and return the path."""
    suffix = os.path.splitext(upload_file.filename)[1]
    with tempfile.NamedTemporaryFile(delete= False, suffix= suffix) as tmp:
        content = upload_file.file.read()
        tmp.write(content)
        return tmp.name
    
def create_temp_zip() -> str:
    """Create and return a temporary zip file path."""
    fd, zip_path = tempfile.mkstemp(suffix=".zip")
    os.close(fd)
    return zip_path

def cleanup_file(path: str):
    try:
        os.remove(path)
    except Exception:
        pass