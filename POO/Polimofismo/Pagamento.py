class Pagamento():
    def processar_pagamento(self):
        pass


class CartaoDeCredito(Pagamento):
    def __init__(self, codigo) -> None:
        super().__init__()
        self.cartao_numero = codigo
    
    def processar_pagamento(self):
        print("Processando pagamento usando cartão de crédito")


class Boleto(Pagamento):
    def __init__(self,codigo) -> None:
        super().__init__()
        self.boleto_numero = codigo
    
    def processar_pagamento(self):
        print("Processando pagamento usando boleto")


class PagamentoPix(Pagamento):
    def __init__(self,codigo) -> None:
        super().__init__()
        self.pix_codigo = codigo
    
    def processar_pagamento(self):
        print("Processando pagamento usando Pix")



if __name__ == '__main__':
    pagamento_cartao_credito = CartaoDeCredito('123')
    pagamento_cartao_credito.processar_pagamento()
    
    pagamento_boleto = Boleto('123')
    pagamento_boleto.processar_pagamento()
    
    pagamento_pix = PagamentoPix('123')
    pagamento_pix.processar_pagamento()
