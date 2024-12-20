import pytest

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_ola():
    response = client.get("/")
    assert response.status_code == 200
    

def test_2_ola():
    response = client.get("/")
    assert response.json() == {"Olá":"Mundo"}

def test_listar_produtos_code():
    response = client.get("/produtos")
    assert response.status_code == 200