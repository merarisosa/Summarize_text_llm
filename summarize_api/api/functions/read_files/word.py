from utils.logs.filehandler import logging
import textract
import tempfile  
import os 

async def read_word(file_content: bytes) -> str:
    output_dir = os.path.join(os.getcwd(), "utils", "output")
    output_text_file = os.path.join(output_dir, "texto.txt")

    try:

        logging.info("Extrayendo texto del documento Word")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
            temp_file.write(file_content)
            temp_file_path = temp_file.name  

        texto = textract.process(temp_file_path)
        texto_output = texto.decode('utf-8')

        with open(output_text_file, "w", encoding="utf-8") as f:
            f.write(texto_output)

        logging.debug(f"Texto extraído del archivo y guardado en: {output_text_file}")
        os.unlink(temp_file_path)
        
        return texto_output
    except Exception as e:
        logging.error(f"Error al extraer texto del archivo Word: {e}")
        return str(e)