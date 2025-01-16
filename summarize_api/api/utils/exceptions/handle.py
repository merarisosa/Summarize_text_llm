from fastapi import HTTPException
from utils.logs.filehandler import logging
from fastapi.responses import JSONResponse

# Handler para errores genéricos
async def handle_exception(e: Exception, message: str):
    logging.error(f"{message}: {str(e)}")
    raise HTTPException(status_code=500, detail="Error interno del servidor")

# Handler para error en controllers
def handle_error(error: Exception, message: str):
    logging.error(message)
    raise HTTPException(status_code=500, detail=str(error))

# Handler para errores de request
async def handle_request_exception(endpoint: str, e: Exception):
    logging.error(f"Error en {endpoint}: {str(e)}")
    return JSONResponse({"error": str(e)}, status_code=500)