from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smatphone",
        "descricao": "telefone",
        "preco": 1500,
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Computador",
        "preco": 3500,
    },
    {
        "id": 3,
        "nome": "Tablet",
        "descricao": "Dispositivo de leitura",
        "preco": 2100,
    },
]

@app.get("/") # Request
def ola():
    return {"Olá":"Mundo"}

@app.get("/produtos")
def listar_produtos():
    return produtos