from functions.model.llm_llama import call_llama
from utils.logs.filehandler import logging

async def controller_consume_ia(template: str, system_template: str):
    logging.info("Controller. Inicia consumo ")    
    return await call_llama(template, system_template)
