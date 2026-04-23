import os
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from ppt_parser import extract_slides
from ai_generator import generate_explanation
from tts_engine import text_to_audio
from slide_converter import ppt_to_images

app = FastAPI()

# 🔥 Absolute upload path (IMPORTANT FIX)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "../uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)

# 🔥 Enable CORS (frontend will work)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 Serve images + audio
app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")


@app.post("/upload/")
async def upload_ppt(file: UploadFile = File(...)):
    # 🔥 Clean filename (avoid spaces issue)
    filename = file.filename.replace(" ", "_")

    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 🔥 Convert PPT → Images
    image_paths = ppt_to_images(file_path, UPLOAD_DIR)

    slides = extract_slides(file_path)

    results = []

    for i, slide in enumerate(slides):
        explanation = generate_explanation(
            slide["title"],
            slide["content"]
        )

        audio_path = text_to_audio(
            explanation,
            f"slide_{slide['slide_number']}"
        )

        results.append({
            "slide": slide["slide_number"],
            "title": slide["title"],
            "explanation": explanation,
            "audio": os.path.basename(audio_path),
            "image": os.path.basename(image_paths[i])
        })

    return {"data": results}