from functions.summary.generate import generate_summary
from functions.read_files.extension import process_file
from schema.summarize import TemplateType
from utils.exceptions.handle import handle_error

# Controlador para generar un resumen
async def controller_generate_summary(text: str, type_template: TemplateType):
    try:
        return await generate_summary(text, type_template)
    except Exception as e:
        handle_error(e, "Error al generar el resumen")

# Controlador para procesar archivos
async def controller_process_file(file_content: bytes, file_path: str):
    try:
        return await process_file(file_path, file_content)
    except Exception as e:
        handle_error(e, f"Error al procesar el archivo {file_path}")