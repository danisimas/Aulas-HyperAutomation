class Veiculo:
    _total_veiculos = 0 

    def __init__(self, nome, ano, valor_diario):
        self.__nome = nome 
        self.__ano = ano 
        self.__valor_diario = valor_diario  
        Veiculo._total_veiculos += 1 

    
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_valor_diario(self):
        return self.__valor_diario

    def set_valor_diario(self, valor_diario):
        self.__valor_diario = valor_diario

    
    
    def calcular_aluguel(self, dias, desconto=0):
        valor_total = self.__valor_diario * dias
        if desconto:
            valor_total -= valor_total * (desconto / 100)
        return valor_total

    @classmethod
    def total_veiculos(cls):
        return cls._total_veiculos

    @classmethod
    def aplicar_aumento(cls, percentual, veiculos):
        for veiculo in veiculos:
            novo_valor = veiculo.get_valor_diario() * (1 + percentual / 100)
            veiculo.set_valor_diario(novo_valor)


class Carro(Veiculo):
    def __init__(self, nome, ano, valor_diario, tipo_combustivel):
        super().__init__(nome, ano, valor_diario)
        self.tipo_combustivel = tipo_combustivel

    def calcular_aluguel(self, dias, desconto=0):
        valor_total = super().calcular_aluguel(dias, desconto)
        if dias > 7:
            valor_total -= valor_total * 0.05  # Aplica desconto extra de 5% para mais de 7 dias
        return valor_total

    def informacao(self):
        return f"Nome: {self.get_nome()}, Ano: {self.get_ano()}, Valor Diário: R${self.get_valor_diario():.2f}, Combustível: {self.tipo_combustivel}"


class Moto(Veiculo):
    def __init__(self, nome, ano, valor_diario, cilindrada):
        super().__init__(nome, ano, valor_diario)
        self.cilindrada = cilindrada

    def calcular_aluguel(self, dias, desconto=0):
        valor_total = super().calcular_aluguel(dias, desconto)
        if self.cilindrada > 200:
            valor_total += valor_total * 0.10  
        return valor_total

    def informacao(self):
        return f"Nome: {self.get_nome()}, Ano: {self.get_ano()}, Valor Diário: R${self.get_valor_diario():.2f}, Cilindrada: {self.cilindrada}cc"



if __name__ == '__main__':

    carro1 = Carro("Fiat Uno", 2020, 100, "Gasolina")
    moto1 = Moto("Honda CB", 2019, 50, 250)

    print(carro1.informacao())
    print(moto1.informacao())

    print(f"Aluguel do carro por 10 dias: R${carro1.calcular_aluguel(10):.2f}")
    print(f"Aluguel da moto por 5 dias: R${moto1.calcular_aluguel(5):.2f}")

    print(f"Total de veículos cadastrados: {Veiculo.total_veiculos()}")

    veiculos = [carro1, moto1]
    Veiculo.aplicar_aumento(10, veiculos)  # Aumento de 10% no valor diário
    print(f"Novo valor diário do carro: R${carro1.get_valor_diario():.2f}")
    print(f"Novo valor diário da moto: R${moto1.get_valor_diario():.2f}")
