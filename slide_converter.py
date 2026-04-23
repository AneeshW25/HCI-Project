import os
import subprocess
from pdf2image import convert_from_path


def ppt_to_images(ppt_path, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Convert PPT → PDF using LibreOffice
    subprocess.run([
        "C:\\Program Files\\LibreOffice\\program\\soffice.exe",
        "--headless",
        "--convert-to", "pdf",
        ppt_path,
        "--outdir", output_folder
    ], check=True)

    # Get correct PDF filename
    base_name = os.path.splitext(os.path.basename(ppt_path))[0]
    pdf_path = os.path.join(output_folder, base_name + ".pdf")

    # 🔴 Safety check (VERY IMPORTANT)
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not created: {pdf_path}")

    # Convert PDF → Images using Poppler
    images = convert_from_path(
        pdf_path,
        poppler_path=r"C:\poppler-25.12.0\Library\bin"
    )

    image_paths = []

    for i, img in enumerate(images):
        img_path = os.path.join(output_folder, f"slide_{i+1}.png")
        img.save(img_path, "PNG")
        image_paths.append(img_path)

    return image_paths