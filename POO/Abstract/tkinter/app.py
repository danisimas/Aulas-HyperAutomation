import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod
import datetime

# Classes de Funcionário
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
        if matricula.strip() == "":
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
import tkinter as tk
from tkinter import ttk, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Funcionários")
        self.root.geometry("800x600")

        self.nome_var = tk.StringVar()
        self.matricula_var = tk.StringVar()
        self.num_proj_var = tk.StringVar()
        self.salario_var = tk.StringVar()
        self.comissao_var = tk.StringVar()
        self.total_vendas_var = tk.StringVar()
        self.valor_hora_var = tk.StringVar()
        self.horas_dia_var = tk.StringVar()

        # Criar o layout
        self.create_widgets()

        self.funcionarios = []

    def create_widgets(self):
        # Seção Dados Pessoais
        dados_pessoais_frame = ttk.LabelFrame(self.root, text="Dados Pessoais")
        dados_pessoais_frame.place(x=10, y=10, width=780, height=200)

        ttk.Label(dados_pessoais_frame, text="Nome").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(dados_pessoais_frame, textvariable=self.nome_var).grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(dados_pessoais_frame, text="Matrícula").grid(row=0, column=2, padx=10, pady=5)
        tk.Entry(dados_pessoais_frame, textvariable=self.matricula_var).grid(row=0, column=3, padx=10, pady=5)

        ttk.Label(dados_pessoais_frame, text="Número de Projetos").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(dados_pessoais_frame, textvariable=self.num_proj_var).grid(row=1, column=1, padx=10, pady=5)

        # Seção Dados Específicos de Funcionário
        funcionario_frame = ttk.LabelFrame(self.root, text="Dados do Funcionário")
        funcionario_frame.place(x=10, y=220, width=780, height=150)

        ttk.Label(funcionario_frame, text="Salário Base").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(funcionario_frame, textvariable=self.salario_var).grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(funcionario_frame, text="Comissão (%)").grid(row=0, column=2, padx=10, pady=5)
        tk.Entry(funcionario_frame, textvariable=self.comissao_var).grid(row=0, column=3, padx=10, pady=5)

        ttk.Label(funcionario_frame, text="Total de Vendas").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(funcionario_frame, textvariable=self.total_vendas_var).grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(funcionario_frame, text="Valor por Hora").grid(row=1, column=2, padx=10, pady=5)
        tk.Entry(funcionario_frame, textvariable=self.valor_hora_var).grid(row=1, column=3, padx=10, pady=5)

        ttk.Label(funcionario_frame, text="Horas por Dia").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(funcionario_frame, textvariable=self.horas_dia_var).grid(row=2, column=1, padx=10, pady=5)

        # Botão de cadastro
        tk.Button(self.root, text="Cadastrar Funcionário", command=self.cadastrar_funcionario).place(x=300, y=400)

        # Botão para processar os pagamentos
        tk.Button(self.root, text="Processar Pagamentos", command=self.processar_pagamentos).place(x=460, y=400)

    def cadastrar_funcionario(self):
        try:
            nome = self.nome_var.get()
            matricula = self.matricula_var.get()
            num_proj = int(self.num_proj_var.get()) if self.num_proj_var.get().strip() else 0
            
            # Verificar qual tipo de funcionário está sendo cadastrado
            if self.salario_var.get() and self.comissao_var.get() and self.total_vendas_var.get():
                # FuncionarioComissario
                salario = float(self.salario_var.get().strip()) if self.salario_var.get().strip() else 0.0
                comissao = float(self.comissao_var.get().strip()) / 100 if self.comissao_var.get().strip() else 0.0
                total_vendas = float(self.total_vendas_var.get().strip()) if self.total_vendas_var.get().strip() else 0.0
                funcionario = FuncionarioComissario(nome, matricula, num_proj, salario, comissao, total_vendas)

            elif self.valor_hora_var.get() and self.horas_dia_var.get():
                # FuncionarioHoralista
                valor_hora = float(self.valor_hora_var.get().strip()) if self.valor_hora_var.get().strip() else 0.0
                horas_dia = float(self.horas_dia_var.get().strip()) if self.horas_dia_var.get().strip() else 0.0
                funcionario = FuncionarioHoralista(nome, matricula, num_proj, valor_hora, horas_dia)

            else:
                # FuncionarioMensalista
                salario = float(self.salario_var.get().strip()) if self.salario_var.get().strip() else 0.0
                funcionario = FuncionarioMensalista(nome, matricula, num_proj, salario)

            # Adicionar o funcionário à lista
            self.funcionarios.append(funcionario)
            messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")

        except ValueError as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar funcionário: {str(e)}")


    def processar_pagamentos(self):
        resultado = ""
        for funcionario in self.funcionarios:
            resultado += f"Funcionário: {funcionario}\nSalário: R$ {funcionario.calcular_salario():.2f}\n{'-'*50}\n"

        messagebox.showinfo("Pagamentos", resultado)

# Função Principal
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = App(root)
    root.mainloop()
