from fastapi import HTTPException
from functions.model.llm_llama import call_llama
from schema.summarize import TemplateType, TEMPLATE_USER_FUNCTIONS, TEMPLATE_SYSTEM_FUNCTIONS
from utils.logs.filehandler import logging

async def generate_summary(text: str, type_template: TemplateType)-> str :
    template_user_function = TEMPLATE_USER_FUNCTIONS.get(type_template)
    template_system_function = TEMPLATE_SYSTEM_FUNCTIONS.get(type_template)
    
    if not template_user_function or not template_system_function:
        raise ValueError(f"Plantilla no encontrada para el tipo: {type_template}")

    result = await call_llama(template_user_function(text), template_system_function)   
    logging.info(f"Resultado de consume_ia: {result}")

    if "error" in result:
        raise HTTPException(status_code=result["status_code"], detail=result["error"])
    if "response" in result:
        return result["response"]
    else:
        raise ValueError("Respuesta malformada, no contiene 'response'")



