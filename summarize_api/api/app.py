from controller.call_ia import controller_consume_ia
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from router import summarize

app = FastAPI()

app.include_router(summarize.router, prefix="/summarize", tags=["summarize"])

@app.get("/")
async def read_root() -> str:
    try:
        user = "Saluda a un usuario"
        system = "Salida en formato JSON"

        response = await controller_consume_ia (user, system)
        return JSONResponse({"saludo": response}, status_code=200)
    except Exception as e:
        return f"Error al iniciar el modelo {e}"

