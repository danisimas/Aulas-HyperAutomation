from functools import reduce

from Excecoes import QuantidadeInvalidaError


class Pedido:
    def __init__(self, produtos, quantidade, cliente, status="Novo"):
        for prod, qtd in quantidade.items():
            if qtd <= 0:
                raise QuantidadeInvalidaError("A quantidade de produtos deve ser positiva.")
        self.produtos = produtos
        self.quantidade = quantidade
        self.cliente = cliente
        self.status = status

    def total_pedido(self):
        return reduce(lambda acc, prod: acc + prod.preco * self.quantidade[prod], self.produtos, 0)

    def detalhes_pedido(self):
        detalhes_produtos = ", ".join(
            f"{prod.detalhes()} (Quantidade: {self.quantidade[prod]})" for prod in self.produtos
        )
        return f"Cliente: {self.cliente}, Status: {self.status}, Produtos: {detalhes_produtos}, Total: {self.total_pedido()}"
