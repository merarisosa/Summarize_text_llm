from functions.api_key.generate import create_api_key
from functions.api_key.verify import verify_api_key
from fastapi import Header, HTTPException
from utils.logs.filehandler import logging

async def controller_generate_api_key():
    return create_api_key()

def controller_verify_api_key(api_key: str = Header(None, alias="api_key")):
    if not api_key:
        logging.error("API Key no proporcionada")
        raise HTTPException(status_code=400, detail="API Key is required")
    logging.info("Verificando API Key...")
    return verify_api_key(api_key)