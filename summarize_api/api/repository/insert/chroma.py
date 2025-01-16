from utils.logs.filehandler import logging
import sqlite3
import os 

base_path = os.getcwd() 
db_path = os.path.join(base_path, "chroma", "chroma.sqlite3")


def insert_api_key_into_db(new_key, hashed_key):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO api_key_users (new_key, hashed_key)
            VALUES (?, ?)
            """,
            (new_key, hashed_key)
        )

        conn.commit()    
    except sqlite3.Error as e:
        logging.error(f"Error al insertar la API Key en la base de datos: {e}")
        raise e  
    finally:
        conn.close()