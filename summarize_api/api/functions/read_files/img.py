import pytesseract
from PIL import Image
from utils.logs.filehandler import logging
import os
import tempfile  
import imghdr

async def read_img(file_content: bytes) -> str:
    try:
        output_dir = os.path.join(os.getcwd(), "utils", "output")
        output_text_file = os.path.join(output_dir, "texto.txt")
        
        output_text_file = os.path.join(output_dir, "texto_extraido.txt")
        img_type = imghdr.what(None, h=file_content)
        
        if not img_type:
            raise ValueError("Tipo de imagen no soportado o no reconocido")

        logging.info("Extrayendo texto de la imagen")

        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{img_type}") as temp_file:
            temp_file.write(file_content)
            temp_file_path = temp_file.name

        text = extract_text_from_image(temp_file_path)
        save_text_to_file(text, output_text_file)

        logging.debug(f"Texto extraído del archivo y guardado en: {output_text_file}")
        os.unlink(temp_file_path)
        
        return text
    except Exception as e:
        logging.error(f"Error al extraer texto del archivo de imagen: {e}", exc_info=True)
        return str(e)

def extract_text_from_image(image_path: str) -> str:
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        logging.error(f"Error al procesar la imagen: {e}", exc_info=True)
        raise

def save_text_to_file(text: str, file_path: str):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        logging.error(f"Error al guardar el texto en el archivo: {e}", exc_info=True)
        raise