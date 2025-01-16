from fastapi import HTTPException, status, Header
from repository.select.chroma import select_api_key_from_db
from utils.logs.filehandler import logging
from keycove import hash

def log_and_raise(log_message: str, status_code: int, detail_message: str):
    logging.info(log_message)
    raise HTTPException(status_code=status_code, detail=detail_message)

def api_key_exists_in_db(hashed_key: str) -> bool:
    result = select_api_key_from_db(hashed_key)
    return bool(result)

def verify_api_key(api_key: str = Header(None, alias="api_key")):
    if api_key is None:
        log_and_raise("API Key Missing", status.HTTP_401_UNAUTHORIZED, "Unauthorized. API Key missing")
    
    hashed_input_key = hash(api_key)
    
    if not api_key_exists_in_db(hashed_input_key):
        log_and_raise("API Key Invalid", status.HTTP_401_UNAUTHORIZED, "API Key inválida")
    
    logging.info("API Key Found")
    return True
