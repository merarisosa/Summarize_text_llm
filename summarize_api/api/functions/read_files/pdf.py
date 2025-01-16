from PyPDF2 import PdfReader
import io
from pdf2image import convert_from_bytes
import pytesseract
from utils.logs.filehandler import logging
import os

async def read_pdf(file_content: bytes) -> str:
    try:
        output_dir = os.path.join(os.getcwd(), "utils", "output")
        output_text_file = os.path.join(output_dir, "texto.txt")
        
        text = extract_text_from_pdf(file_content)
        save_text_to_file(text, output_text_file)
        
        logging.debug(f"Texto extraído del archivo y guardado en: {output_text_file}")
        return text
    except Exception as e:
        logging.error(f"Error al extraer texto del archivo PDF: {e}", exc_info=True)
        return str(e)

def create_output_directory() -> str:
    output_dir = os.path.join(os.getcwd(), "utils", "outputs")
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def extract_text_from_pdf(file_content: bytes) -> str:
    pdf_file = io.BytesIO(file_content)
    pdf_reader = PdfReader(pdf_file)
    logging.info("Extrayendo contenido del PDF")
    
    text = ''
    for page_num, page in enumerate(pdf_reader.pages):
        page_text = page.extract_text()
        
        if page_text and page_text.strip():
            text += page_text
        else:
            text += extract_text_from_images(file_content)
    
    return text

def extract_text_from_images(file_content: bytes) -> str:
    """Convierte las páginas de un archivo PF a imágenes y extrae el texto usando OCR."""
    images = convert_from_bytes(file_content)
    text = ''
    for image in images:
        ocr_text = pytesseract.image_to_string(image)
        text += ocr_text + "\n"
    return text

def save_text_to_file(text: str, file_path: str):
    try:
        with open(file_path, "w", encoding="utf-8") as text_file:
            text_file.write(text)
    except Exception as e:
        logging.error(f"Error al guardar el texto en el archivo: {e}", exc_info=True)
        raise