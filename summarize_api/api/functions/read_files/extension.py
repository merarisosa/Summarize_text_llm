from functions.read_files.pdf import read_pdf 
from functions.read_files.word import read_word 
from functions.read_files.img import read_img 
from functions.read_files.txt import read_txt 
from functions.read_files.pptx import read_pptx 
from functions.read_files.eml import read_eml

async def process_file(file_content: bytes, filename: str) -> str:     
    ext = filename.split('.')[-1].lower()     
    if ext == "pdf":         
        return await read_pdf(file_content)      
    elif ext in ["docx", "doc"]:         
        return await read_word(file_content)     
    elif ext in ["jpg", "jpeg", "png"]:         
        return await read_img(file_content)      
    elif ext in ["txt"]:         
        return await read_txt(file_content)     
    elif ext in ["pptx"]:         
        return await read_pptx(file_content)    
    elif ext in ["eml"]:
        return await read_eml(filename)
    else:         
        raise ValueError("Tipo de archivo no soportado") 