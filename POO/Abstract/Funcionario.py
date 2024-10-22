from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    @abstractmethod
    def calcular_salario(self):
        pass
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        if nome.strip() == "":
            raise ValueError("Nome inválido")
        self._nome = nome
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula):
        if matricula.strip() == "":
            raise ValueError("Matrícula inválida")
        self._matricula = matricula
    

    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}"

class FuncionarioComissario(Funcionario):
    def __init__(self, nome, matricula, salarioBase, comissao, totalVendas):
        super().__init__(nome, matricula)
        self.comissao = comissao
        self.totalVendas = totalVendas
        self.salarioBase = salarioBase


    
    def calcular_salario(self):
        return self.salarioBase + (self.comissao * self.totalVendas)
    
    def __str__(self):
        return super().__str__() + f", Salário Base: {self.salarioBase}, Comissão: {self.comissao}, Total de Vendas: {self.totalVendas}"

class FuncionarioHoralista(Funcionario):
    def __init__(self, nome, matricula, salarioBase, horasTrabalhadas):
        super().__init__(nome, matricula)
        self.salarioBase = salarioBase
        self.horasTrabalhadas = horasTrabalhadas
    
    def calcular_salario(self):
        return self.salarioBase * self.horasTrabalhadas
    
    def __str__(self):
        return super().__str__() + f", Salário Base: {self.salarioBase}, Horas Trabalhadas: {self.horasTrabalhadas}"

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, matricula, salarioBase):
        super().__init__(nome, matricula)
        self.salarioBase = salarioBase
    
    def calcular_salario(self):
        return self.salarioBase
    
    def __str__(self):
        return super().__str__() + f", Salário Base: {self.salarioBase}"
    

def processar_pagamentos():
    funcionarios = [
        FuncionarioComissario("Daniele", "123", 5000, 0.1, 10000),
        FuncionarioHoralista("Luiz", "456", 6000, 40),
        FuncionarioMensalista("Carlos", "789", 7000)
    ]
    
    for funcionario in funcionarios:
        print(f"Funcionário: {funcionario}")
        print(f"Salário: R$ {funcionario.calcular_salario():.2f}")
        print("-" * 50)





if __name__ == "__main__":
    processar_pagamentos()