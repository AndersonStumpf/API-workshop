from typing import List, Dict

class Produtos:
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
    def listar_produtos(self):
        return self.produtos
    
    def buscar_produto(self, id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status": 404, "Mensagem": "Produto não encontrado."}
    
    def adicionar_produtos(self, produto):
        self.produtos.append(produto)
        return produto