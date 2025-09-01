# 📄 PDF Extractor API

A modular **FastAPI backend** that extracts **text, tables, and images** from uploaded PDF files.  
The extracted content is returned as a **ZIP file** containing:

- ✅ `text.txt` – extracted text  
- ✅ `table_X.csv` – tables saved as CSV (without using pandas, lightweight CSV writer)  
- ✅ extracted image files (`image_1.png`, `image_2.png`, …)  

This project is designed with **clean modular structure**, **Dockerized deployment**, and can be consumed easily by any frontend (e.g., Streamlit).

---

## ⚡ Features
- Upload a PDF via REST API  
- Extract:
  - Text (saved in `.txt`)  
  - Tables (saved in `.csv` without pandas, using Python’s built-in `csv`)  
  - Images (saved as `.png`)  
- Get everything in a **single downloadable ZIP file**  
- Modular project structure (services, utils, routes)  
- Dockerized for easy deployment  

---

## 📂 Project Structure
```
pdf-extractor-backend/
│── app/
│   ├── main.py                 # FastAPI entrypoint
│   ├── routes/
│   │   └── extract.py          # API endpoint
│   ├── services/
│   │   └── extractor.py        # PDF extraction logic
│   ├── utils/
│   │   └── file_ops.py         # File saving helpers
│── requirements.txt            # Python dependencies
│── Dockerfile                  # Container build file
│── README.md                   # Documentation
```

---

## 🛠️ Installation (Local)

### 1. Clone repository
```bash
git clone https://github.com/Dipesh-Ydv/pdf-extractor-backend-api.git
cd pdf-extractor-backend
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run FastAPI server
```bash
uvicorn app.main:app --reload
```

### 4. Open API Docs
Go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📦 API Usage

### Endpoint
```
POST /extract/pdf
```

### Request (multipart/form-data)
Upload a PDF file with the key `file`.

Example using `curl`:
```bash
curl -X POST "http://127.0.0.1:8000/extract/pdf" \
  -F "file=@sample.pdf" \
  -o output.zip
```

### Response
- Returns a **ZIP file** containing:
  - `text.txt`
  - `table_1.csv`, `table_2.csv`, …
  - `image_1.png`, `image_2.png`, …

---

## 🐳 Docker Setup

### 1. Build Docker Image
```bash
docker build -t pdf-extractor-backend .
```

### 2. Run Container
```bash
docker run -d -p 8000:8000 pdf-extractor-backend
```

Now API is available at:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🚀 Push to Docker Hub

### 1. Tag image
```bash
docker tag pdf-extractor-backend:latest dipeshydv/pdf-extractor-backend:latest
```

### 2. Push
```bash
docker push dipeshydv/pdf-extractor-backend:latest
```

### 3. Pull (on server/other machine)
```bash
docker pull dipeshydv/pdf-extractor-backend:latest
docker run -d -p 8000:8000 dipeshydv/pdf-extractor-backend:latest
```

---

## 📋 Requirements
See [`requirements.txt`](requirements.txt):
```
fastapi
uvicorn[standard]
python-multipart
pdfplumber
pillow
pandas
zipfile36
pyMuPdf
```

---

## 🤝 Contributing
1. Fork the project  
2. Create a feature branch (`git checkout -b feature/xyz`)  
3. Commit changes (`git commit -m 'Add xyz'`)  
4. Push to branch (`git push origin feature/xyz`)  
5. Create a Pull Request  

---

## 📜 License
MIT License – free to use & modify.
