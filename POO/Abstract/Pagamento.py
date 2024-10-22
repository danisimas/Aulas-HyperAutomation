from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
       pass 

    def detalhes_pagamento(self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento com cartão de crédito. Valor: R$ {valor}")
        self.detalhes_pagamento(valor)
    
    def detalhes_pagamento(self, valor):
        print("Detalhes do pagamento:")
        print(f"- Cartão de crédito: XXXX-XXXX-XXXX")
        print(f"- Bandeira: Visa")
        print(f"- Validade: 12/24")
        print(f"- Titular: John Doe")
        print(f"- Quantidade de parcelas: 1")
        print(f"- Valor da parcela: R$ {valor / 1}")
        print(f"- Taxa de juros: 0%")
        print(f"- Total do pagamento: R$ {valor}")

class Boleto(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento com boleto. Valor: R$ {valor}")
        self.detalhes_pagamento(valor)
    
    def detalhes_pagamento(self, valor):
        print("Detalhes do pagamento:")
        print(f"- Número do boleto: 1234567890")
        print(f"- Data de vencimento: 01/12")
        print(f"- Valor do boleto: R$ {valor}")




def testar_pagamentos():
    pagamentos = [
        CartaoCredito(),
        Boleto(),
    ]
    
    for pagamento in pagamentos:
        pagamento.processar_pagamento(100)

if __name__ == "__main__":
    testar_pagamentos()
