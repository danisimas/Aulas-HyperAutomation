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


'''

1. O que acontece se você adicionar um novo método de pagamento sem
modificar a função processar?

R = Ela não vai existir, se não modificar ou vai pegar o valor do método pai dela

2. Como o polimorfismo ajuda a manter o código flexível e extensível?

R = Ele permite que subclasses implementem métodos que se comportam de maneira diferente, sem alterar o comportamento do método pai.
Então, ele permite a flexibilidade do código junto com a extensão.

3. Qual é a diferença entre a função processar e os métodos
processar_pagamento nas subclasses?

R = A diferença é a função processar pagamento na classe pai está vazia, ja nas subclasses, reescrevemos
com o contexto de cada pagamento conforme sua classe.

4. Como você pode garantir que todos os métodos de pagamento
implementem o método processar_pagamento corretamente?

R = Fazendo a herança da classe as subclasses.

'''