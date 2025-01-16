from fastapi import APIRouter, UploadFile, HTTPException, Depends
from fastapi.responses import JSONResponse
from controller.summarize import (
    controller_generate_summary, 
    controller_process_file
)
from schema.summarize import TextSummary, TemplateType
from controller.api_key import controller_verify_api_key
from utils.logs.filehandler import logging
from schema.summarize import Peticion
from utils.exceptions.handle import handle_exception

router = APIRouter()

# resumen de texto
@router.post("/texto")
async def app_summarize_texto(summary: TextSummary, authenticated: bool = Depends(controller_verify_api_key)) -> JSONResponse:
    logging.info("Inicia petición POST /texto")
    try:
        response = await controller_generate_summary(summary.text, summary.type_template)
        return JSONResponse({"summary": response}, status_code=200)
    except Exception as e:
        await handle_exception(e, "Error inesperado en /texto")

# procesar y resumir archivos
@router.post("/files")
async def app_summarize_file(file: UploadFile, type_template: TemplateType, authenticated: bool = Depends(controller_verify_api_key)) -> JSONResponse:
    logging.info("Inicia petición POST /files")
    try:
        if not file:
            raise HTTPException(status_code=400, detail="Debe proporcionar un archivo válido.")

        file_content = await file.read()
        content = await controller_process_file(file_content, file.filename)
        response = await controller_generate_summary(content, type_template)
        return JSONResponse({"summary_file": response}, status_code=200)
    except HTTPException as e:
        raise e
    except Exception as e:
        await handle_exception(e, "Error al procesar el archivo en /files")
   
    