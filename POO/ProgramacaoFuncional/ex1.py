class Vendas():
    def __init__(self, nome_produto, qutde_vendida, preco_unit):
        self.nome_produto = nome_produto
        self.qutde_vendida = qutde_vendida
        self.preco_unit = preco_unit
    
        

class HistoricoVenda(Vendas):
    def __init__(self, nome_produto, qutde_vendida, preco_unit, data_venda):
        super().__init__(nome_produto, qutde_vendida, preco_unit)
        self.data_venda = data_venda
    

