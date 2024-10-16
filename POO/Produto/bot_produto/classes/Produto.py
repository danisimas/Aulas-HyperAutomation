class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
    
    def atualizar_produto(self, produto):
        self.nome = produto.nome
        self.preco = produto.preco
        self.quantidade = produto.quantidade
    
    



# if __name__ == "__main__":
#     produto1 = Produto("Notebook", 3000.00, 10)
#     produto1.mostrar_dados()
    
#     produto2 = Produto("Mouse", 20.00, 50)
#     produto1.atualizar_produto(produto2)
#     produto1.mostrar_dados()
    
