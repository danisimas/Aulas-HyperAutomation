from abc import ABC, abstractmethod
import datetime

class Funcionario(ABC):
    def __init__(self, nome, matricula, numero_de_projetos):
        self.nome = nome
        self.matricula = matricula
        self.numero_de_projetos = numero_de_projetos
    
    @abstractmethod
    def calcular_salario(self):
        pass
    
    def calcular_pd(self):
        if self.numero_de_projetos > 0:
            return self.numero_de_projetos * 1000
        return 0

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
        if matricula is None:
            raise ValueError("Matrícula inválida")
        self._matricula = matricula
    
    @property
    def numero_de_projetos(self):
        return self._numero_de_projetos
    
    @numero_de_projetos.setter
    def numero_de_projetos(self, numero_de_projetos):
        if numero_de_projetos < 0:
            raise ValueError("Número de projetos não pode ser negativo")
        self._numero_de_projetos = numero_de_projetos
    
    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Número de projetos: {self.numero_de_projetos}"


class FuncionarioComissario(Funcionario):
    def __init__(self, nome, matricula, numero_de_projetos, salario_base, comissao, total_vendas):
        super().__init__(nome, matricula, numero_de_projetos)
        self.salario_base = salario_base
        self.comissao = comissao
        self.total_vendas = total_vendas

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        if salario_base <= 0:
            raise ValueError("Salário base deve ser maior que zero")
        self._salario_base = salario_base
    
    def calcular_salario(self):
        if self.total_vendas <= 0 or self.comissao <= 0:
            raise ValueError("Total de vendas e comissão precisam ser maiores que zero")
        salario = self.salario_base + (self.comissao * self.total_vendas)
        salario += self.calcular_pd()
        return salario
    
    def __str__(self):
        return super().__str__() + f", Salário Base: {self.salario_base}, Comissão: {self.comissao}, Total de Vendas: {self.total_vendas}"


class FuncionarioHoralista(Funcionario):
    def __init__(self, nome, matricula, numero_de_projetos, valor_por_hora, horas_por_dia):
        super().__init__(nome, matricula, numero_de_projetos)
        self.valor_por_hora = valor_por_hora
        self.horas_por_dia = horas_por_dia

    @property
    def valor_por_hora(self):
        return self._valor_por_hora

    @valor_por_hora.setter
    def valor_por_hora(self, valor_por_hora):
        if valor_por_hora <= 0:
            raise ValueError("Valor por hora deve ser maior que zero")
        self._valor_por_hora = valor_por_hora

    @property
    def horas_por_dia(self):
        return self._horas_por_dia

    @horas_por_dia.setter
    def horas_por_dia(self, horas_por_dia):
        if horas_por_dia <= 0:
            raise ValueError("Horas por dia deve ser maior que zero")
        self._horas_por_dia = horas_por_dia

    def simular_pagamento_mensal(self, ano, mes):
        dias_no_mes = (datetime.date(ano, mes % 12 + 1, 1) - datetime.timedelta(days=1)).day
        total_horas_trabalhadas = self.horas_por_dia * dias_no_mes
        salario_total = self.valor_por_hora * total_horas_trabalhadas
        return salario_total
    
    def calcular_salario(self):
        salario = self.simular_pagamento_mensal(2024, 10)
        salario += self.calcular_pd()
        return salario
    
    def __str__(self):
        return super().__str__() + f", Valor Por Hora: {self.valor_por_hora}, Horas Por Dia: {self.horas_por_dia}"


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, matricula, numero_de_projetos, salario_base):
        super().__init__(nome, matricula, numero_de_projetos)
        self.salario_base = salario_base

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        if salario_base <= 0:
            raise ValueError("Salário base deve ser maior que zero")
        self._salario_base = salario_base
    
    def calcular_salario(self):
        salario = self.salario_base
        salario += self.calcular_pd()
        return salario
    
    def __str__(self):
        return super().__str__() + f", Salário Base: {self.salario_base}"


def processar_pagamentos():
    funcionarios = [
        FuncionarioComissario("Daniele", "123", 0, 5000, 0.1, 10000), 
        FuncionarioHoralista("Luiz", "456", 0, 50, 8), 
        FuncionarioMensalista("Carlos", "789", 1, 7000)  
    ]
    
    for funcionario in funcionarios:
        print(f"Funcionário: {funcionario}")
        print(f"Salário: R$ {funcionario.calcular_salario():.2f}")
        print("-" * 50)


if __name__ == "__main__":
    processar_pagamentos()
