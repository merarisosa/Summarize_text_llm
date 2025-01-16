import sqlite3
import os

base_path = os.getcwd()
db_path = os.path.join(base_path, "chroma", "chroma.sqlite3")

def select_api_key_from_db(hashed_key: str):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM api_key_users WHERE hashed_key = ?
            """, (hashed_key,)
        )

        result = cursor.fetchone()
        return result  
    except sqlite3.Error as e:
        raise Exception(f"Error al consultar la base de datos: {e}")
    finally:
        conn.close()
        
