import fitz
import pdfplumber
import pandas
import zipfile

def extract_text_tables_images(file_path: str, zip_path: str) -> str:
    """Extract text, tables and images from a PDF file and write them into a ZIP archive.
    Returns the path to the ZIP file.
    """
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        all_text = ""

        # Extract text and tables using pdfplumber
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                try:
                    page_text = page.extract_text() or ""
                except Exception:
                    page_text = ""
                if page_text:
                    all_text += f"---- Page {page_num} ----\n{page_text}\n\n"

                # extract tables
                try:
                    tables = page.extract_tables()
                except Exception:
                    tables = None
                if tables:
                    for tbl_idx, tbl in enumerate(tables, start=1):
                        try:
                            df = pandas.DataFrame(tbl)
                            csv_str = df.to_csv(index=False)
                            fname = f"tables/page{page_num}_table{tbl_idx}.csv"
                            zipf.writestr(fname, csv_str)
                        except Exception:
                            continue

        # Write all text to file in ZIP
        if all_text:
            zipf.writestr("text/full_text.txt", all_text)

        # Extract images using PyMuPDF (fitz)
        doc = fitz.open(file_path)
        for page_index in range(len(doc)):
            page = doc[page_index]
            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list, start=1):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                ext = base_image.get('ext', 'png')
                fname = f"images/page{page_index+1}_img{img_index}.{ext}"
                zipf.writestr(fname, image_bytes)

    return zip_path