from utils.logs.filehandler import logging

async def read_txt (file_content: bytes) -> str:
    try:          
        return file_content.decode("utf-8")          
    except Exception as e:
        logging.error(f"Error al procesar el archivo: {str(e)}")
