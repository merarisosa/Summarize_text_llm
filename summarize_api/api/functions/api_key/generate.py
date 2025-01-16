from keycove import generate_token, hash
from repository.insert.chroma import insert_api_key_into_db
from utils.logs.filehandler import logging

def create_api_key():
    new_key = generate_token(num_bytes=16)    
    hashed_key = hash(new_key)
    insert_api_key_into_db(new_key, hashed_key)
    return f"API Key: {new_key} "
