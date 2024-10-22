from abc import ABC, abstractmethod
import datetime

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
        self.salarioBase = salarioBase
        self.comissao = comissao
        self.totalVendas = totalVendas

    @property
    def salarioBase(self):
        return self._salarioBase

    @salarioBase.setter
    def salarioBase(self, salarioBase):
        if salarioBase <= 0:
            raise ValueError("Salário base deve ser maior que zero")
        self._salarioBase = salarioBase
    
    @property
    def comissao(self):
        return self._comissao
    
    @comissao.setter
    def comissao(self, comissao):
        if comissao < 0 or comissao > 1:
            raise ValueError("Comissão deve ser um valor entre 0 e 1")
        self._comissao = comissao
    
    @property
    def totalVendas(self):
        return self._totalVendas
    
    @totalVendas.setter
    def totalVendas(self, totalVendas):
        if totalVendas < 0:
            raise ValueError("Total de vendas não pode ser negativo")
        self._totalVendas = totalVendas


    def calcular_salario(self):
        if self.totalVendas <= 0 or self.comissao <= 0:
            raise ValueError("Total de vendas e comissão precisam ser maiores que zero")
        return self.salarioBase + (self.comissao * self.totalVendas)
    
    def __str__(self):
        return super().__str__() + f", Salário Base: {self.salarioBase}, Comissão: {self.comissao}, Total de Vendas: {self.totalVendas}"

class FuncionarioHoralista(Funcionario):
    def __init__(self, nome, matricula, valorPorHora, horasPorDia):
        super().__init__(nome, matricula)
        self.valorPorHora = valorPorHora 
        self.horasPorDia = horasPorDia

    @property
    def valorPorHora(self):
        return self._valorPorHora

    @valorPorHora.setter
    def valorPorHora(self, valorPorHora):
        if valorPorHora <= 0:
            raise ValueError("Valor por hora deve ser maior que zero")
        self._valorPorHora = valorPorHora

    @property
    def horasPorDia(self):
        return self._horasPorDia

    @horasPorDia.setter
    def horasPorDia(self, horasPorDia):
        if horasPorDia <= 0:
            raise ValueError("Horas por dia deve ser maior que zero")
        self._horasPorDia = horasPorDia

    def simular_pagamento_mensal(self, ano, mes):
        feriados = [
            datetime.date(ano, 1, 1),   # Ano Novo
            datetime.date(ano, 9, 7),   # Independência
            datetime.date(ano, 12, 25), # Natal
            datetime.date(ano, 10, 24), # Aniversário de mANAUS
            datetime.date(ano, 10, 28)  # Dia do Funcionário Público
        ]

        dias_no_mes = (datetime.date(ano, mes % 12 + 1, 1) - datetime.timedelta(days=1)).day
        
        total_horas_trabalhadas = 0
        for dia in range(1, dias_no_mes + 1):
            data_atual = datetime.date(ano, mes, dia)
            total_horas_trabalhadas += self.horasPorDia

        salarioTotal = self.valorPorHora * total_horas_trabalhadas
        return salarioTotal

    def calcular_salario(self):
        return self.simular_pagamento_mensal(2024, 10)
    
    def __str__(self):
        return super().__str__() + f", Valor Por Hora: {self.valorPorHora}, Horas Por Dia: {self.horasPorDia}"

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, matricula, salarioBase):
        super().__init__(nome, matricula)
        self.salarioBase = salarioBase

    @property
    def salarioBase(self):
        return self._salarioBase

    @salarioBase.setter
    def salarioBase(self, salarioBase):
        if salarioBase <= 0:
            raise ValueError("Salário base deve ser maior que zero")
        self._salarioBase = salarioBase
    
    def calcular_salario(self):
        return self.salarioBase
    
    def __str__(self):
        return super().__str__() + f", Salário Base: {self.salarioBase}"
    

def processar_pagamentos():
    funcionarios = [
        FuncionarioComissario("Daniele", "123", 5000, 0.1, 10000),
        FuncionarioHoralista("Luiz", "456", 50, 8),  
        FuncionarioMensalista("Carlos", "789", 7000)
    ]
    
    for funcionario in funcionarios:
        print(f"Funcionário: {funcionario}")
        print(f"Salário: R$ {funcionario.calcular_salario():.2f}")
        print("-" * 50)

if __name__ == "__main__":
    processar_pagamentos()
