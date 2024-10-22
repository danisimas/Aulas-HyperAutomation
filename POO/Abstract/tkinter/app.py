import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod
import datetime
import json
import pandas as pd

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
        self.tipo_funcionario_var = tk.StringVar(value="Mensalista")

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

        # Seção Tipo de Funcionário
        tipo_frame = ttk.LabelFrame(self.root, text="Tipo de Funcionário")
        tipo_frame.place(x=10, y=220, width=780, height=50)

        ttk.Label(tipo_frame, text="Selecionar Tipo").grid(row=0, column=0, padx=10, pady=5)
        tipo_combobox = ttk.Combobox(tipo_frame, textvariable=self.tipo_funcionario_var, 
                                      values=["Comissário", "Horalista", "Mensalista"], state="readonly")
        tipo_combobox.grid(row=0, column=1, padx=10, pady=5)
        tipo_combobox.bind("<<ComboboxSelected>>", self.atualizar_campos)

        # Seção Dados Específicos de Funcionário
        funcionario_frame = ttk.LabelFrame(self.root, text="Dados do Funcionário")
        funcionario_frame.place(x=10, y=270, width=780, height=150)

        ttk.Label(funcionario_frame, text="Salário Base").grid(row=0, column=0, padx=10, pady=5)
        self.salario_entry = tk.Entry(funcionario_frame, textvariable=self.salario_var)
        self.salario_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(funcionario_frame, text="Comissão (%)").grid(row=0, column=2, padx=10, pady=5)
        self.comissao_entry = tk.Entry(funcionario_frame, textvariable=self.comissao_var)
        self.comissao_entry.grid(row=0, column=3, padx=10, pady=5)

        ttk.Label(funcionario_frame, text="Total de Vendas").grid(row=1, column=0, padx=10, pady=5)
        self.total_vendas_entry = tk.Entry(funcionario_frame, textvariable=self.total_vendas_var)
        self.total_vendas_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(funcionario_frame, text="Valor por Hora").grid(row=1, column=2, padx=10, pady=5)
        self.valor_hora_entry = tk.Entry(funcionario_frame, textvariable=self.valor_hora_var)
        self.valor_hora_entry.grid(row=1, column=3, padx=10, pady=5)

        ttk.Label(funcionario_frame, text="Horas por Dia").grid(row=2, column=0, padx=10, pady=5)
        self.horas_dia_entry = tk.Entry(funcionario_frame, textvariable=self.horas_dia_var)
        self.horas_dia_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botão de cadastro
        tk.Button(self.root, text="Cadastrar Funcionário", command=self.cadastrar_funcionario).place(x=300, y=430)

        # Botão para processar os pagamentos
        tk.Button(self.root, text="Processar Pagamentos", command=self.processar_pagamentos).place(x=460, y=430)

        # Atualiza os campos com base no tipo selecionado inicialmente
        self.atualizar_campos()

    def atualizar_campos(self, event=None):
        tipo = self.tipo_funcionario_var.get()
        if tipo == "Comissário":
            self.salario_entry.config(state="normal")
            self.comissao_entry.config(state="normal")
            self.total_vendas_entry.config(state="normal")
            self.valor_hora_entry.config(state="disabled")
            self.horas_dia_entry.config(state="disabled")
        elif tipo == "Horalista":
            self.salario_entry.config(state="disabled")
            self.comissao_entry.config(state="disabled")
            self.total_vendas_entry.config(state="disabled")
            self.valor_hora_entry.config(state="normal")
            self.horas_dia_entry.config(state="normal")
        else:  # Mensalista
            self.salario_entry.config(state="normal")
            self.comissao_entry.config(state="disabled")
            self.total_vendas_entry.config(state="disabled")
            self.valor_hora_entry.config(state="disabled")
            self.horas_dia_entry.config(state="disabled")

    def cadastrar_funcionario(self):
        try:
            nome = self.nome_var.get()
            matricula = self.matricula_var.get()
            num_proj = int(self.num_proj_var.get()) if self.num_proj_var.get().strip() else 0
            
            tipo = self.tipo_funcionario_var.get()
            if tipo == "Comissário":
                salario = float(self.salario_var.get()) if self.salario_var.get().strip() else 0.0
                comissao = float(self.comissao_var.get()) / 100 if self.comissao_var.get().strip() else 0.0
                total_vendas = float(self.total_vendas_var.get()) if self.total_vendas_var.get().strip() else 0.0
                funcionario = FuncionarioComissario(nome, matricula, num_proj, salario, comissao, total_vendas)

            elif tipo == "Horalista":
                valor_hora = float(self.valor_hora_var.get()) if self.valor_hora_var.get().strip() else 0.0
                horas_dia = float(self.horas_dia_var.get()) if self.horas_dia_var.get().strip() else 0.0
                funcionario = FuncionarioHoralista(nome, matricula, num_proj, valor_hora, horas_dia)

            else:  # Mensalista
                salario = float(self.salario_var.get()) if self.salario_var.get() else 0.0
                funcionario = FuncionarioMensalista(nome, matricula, num_proj, salario)

            # Adicionar o funcionário à lista e salvar em um arquivo
            self.funcionarios.append(funcionario)
            self.salvar_funcionario(funcionario)
            messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")

        except ValueError as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar funcionário: {str(e)}")

    def salvar_funcionario(self, funcionario):
        # Salvar os dados do funcionário em um arquivo JSON
        data = {
            "nome": funcionario.nome,
            "matricula": funcionario.matricula,
            "numero_de_projetos": funcionario.numero_de_projetos,
            "salario_base": getattr(funcionario, 'salario_base', None),
            "comissao": getattr(funcionario, 'comissao', None),
            "total_vendas": getattr(funcionario, 'total_vendas', None),
            "valor_por_hora": getattr(funcionario, 'valor_por_hora', None),
            "horas_por_dia": getattr(funcionario, 'horas_por_dia', None)
        }

        try:
            with open('funcionarios.json', 'a') as f:
                f.write(json.dumps(data) + '\n')
        except IOError as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {str(e)}")
    
    def processar_pagamentos(self):
        resultado = ""
        for funcionario in self.funcionarios:
            resultado += f"Funcionário: {funcionario}\nSalário: R$ {funcionario.calcular_salario()}\n{'-'*50}\n"

        messagebox.showinfo("Pagamentos", resultado)


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = App(root)
    root.mainloop()
