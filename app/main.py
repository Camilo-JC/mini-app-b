from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from starlette.requests import Request

from app import servicios

app = FastAPI()
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


class RespuestaRequest(BaseModel):
    id: int
    opcion: Annotated[int, Field(ge=0, le=3)]


@app.get("/")
def pagina_principal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.get("/api/preguntas")
def obtener_preguntas():
    return servicios.obtener_preguntas()


@app.post("/api/responder")
def responder(respuesta: RespuestaRequest):
    resultado = servicios.responder(respuesta.id, respuesta.opcion)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    return resultado
