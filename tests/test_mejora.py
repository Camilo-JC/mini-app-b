from fastapi.testclient import TestClient

from app.main import app

cliente = TestClient(app)


def test_cantidad_predeterminada_devuelve_cinco_preguntas():
    respuesta = cliente.get("/api/preguntas")

    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 5


def test_cantidad_solicitada_limita_las_preguntas():
    for cantidad in (1, 2, 4, 5):
        respuesta = cliente.get(
            "/api/preguntas",
            params={"cantidad": cantidad},
        )

        assert respuesta.status_code == 200
        assert len(respuesta.json()) == cantidad


def test_cantidad_fuera_de_rango_devuelve_422():
    for cantidad in (0, 6):
        respuesta = cliente.get(
            "/api/preguntas",
            params={"cantidad": cantidad},
        )

        assert respuesta.status_code == 422


def test_pagina_permite_elegir_cantidad():
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    assert 'id="cantidad"' in respuesta.text
    assert 'id="iniciar"' in respuesta.text
    assert "/api/preguntas?cantidad=" in respuesta.text
