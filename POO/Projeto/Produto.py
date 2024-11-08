from Excecoes import ValorInvalidoError

class Produto:
    def __init__(self, nome, preco, categoria):
        if preco <= 0:
            raise ValorInvalidoError("O preço do produto deve ser positivo.")
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def detalhes(self):
        return f"Produto: {self.nome}, Preço: {self.preco}, Categoria: {self.categoria}"
