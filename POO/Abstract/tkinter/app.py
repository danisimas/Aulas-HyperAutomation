import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod
import datetime
import json
import pandas as pd


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
        salario = self.salario_base + ((self.comissao / 100 ) * self.total_vendas)
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


def calcular_salario(funcionario):
    if isinstance(funcionario, FuncionarioComissario):
        salario = funcionario.calcular_salario()
        
    elif isinstance(funcionario, FuncionarioHoralista):
        salario = funcionario.calcular_salario()
        
    elif isinstance(funcionario, FuncionarioMensalista):
        salario = funcionario.calcular_salario()
    else:
        print("Tipo de funcionário não reconhecido")
    return salario




class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Funcionários")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f5")

        self.nome_var = tk.StringVar()
        self.matricula_var = tk.StringVar()
        self.num_proj_var = tk.StringVar()
        self.salario_var = tk.StringVar()
        self.comissao_var = tk.StringVar()
        self.total_vendas_var = tk.StringVar()
        self.valor_hora_var = tk.StringVar()
        self.horas_dia_var = tk.StringVar()
        self.tipo_funcionario_var = tk.StringVar(value="Mensalista")

        self.funcionarios = []

        # Criar o layout
        self.create_widgets()
    

    def create_widgets(self):
        # Título
        title = tk.Label(self.root, text="Cadastro de Funcionários", font=("Helvetica", 16, "bold"), bg="#f5f5f5")
        title.pack(pady=10)

        # Seção Dados Pessoais
        dados_pessoais_frame = ttk.LabelFrame(self.root, text="Dados Pessoais", padding=10)
        dados_pessoais_frame.pack(pady=10, padx=20, fill=tk.X)

        self.nome_entry = self.create_label_entry(dados_pessoais_frame, "Nome", self.nome_var, 0, 0)
        self.matricula_entry = self.create_label_entry(dados_pessoais_frame, "Matrícula", self.matricula_var, 0, 2)
        self.num_proj_entry = self.create_label_entry(dados_pessoais_frame, "Número de Projetos", self.num_proj_var, 1, 0)

        # Seção Tipo de Funcionário
        tipo_frame = ttk.LabelFrame(self.root, text="Tipo de Funcionário", padding=10)
        tipo_frame.pack(pady=10, padx=20, fill=tk.X)

        tk.Label(tipo_frame, text="Selecionar Tipo", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        tipo_combobox = ttk.Combobox(tipo_frame, textvariable=self.tipo_funcionario_var,
                                     values=["Comissário", "Horalista", "Mensalista"], state="readonly")
        tipo_combobox.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        tipo_combobox.bind("<<ComboboxSelected>>", self.atualizar_campos)

        # Seção Dados Específicos de Funcionário
        funcionario_frame = ttk.LabelFrame(self.root, text="Dados do Funcionário", padding=10)
        funcionario_frame.pack(pady=10, padx=20, fill=tk.X)

        self.salario_entry = self.create_label_entry(funcionario_frame, "Salário Base", self.salario_var, 0, 0)
        self.comissao_entry = self.create_label_entry(funcionario_frame, "Comissão (%)", self.comissao_var, 0, 2)
        self.total_vendas_entry = self.create_label_entry(funcionario_frame, "Total de Vendas", self.total_vendas_var, 1, 0)
        self.valor_hora_entry = self.create_label_entry(funcionario_frame, "Valor por Hora", self.valor_hora_var, 1, 2)
        self.horas_dia_entry = self.create_label_entry(funcionario_frame, "Horas por Dia", self.horas_dia_var, 2, 0)

        # Botões na parte inferior
        button_frame = tk.Frame(self.root, bg="#f5f5f5")
        button_frame.pack(pady=20)

        cadastrar_btn = tk.Button(button_frame, text="Cadastrar Funcionário", bg="#32CD32", fg="white",
                                  font=("Helvetica", 12, "bold"), relief=tk.FLAT, command=self.cadastrar_funcionario)
        cadastrar_btn.grid(row=0, column=0, padx=10)

        processar_btn = tk.Button(button_frame, text="Processar Pagamentos", bg="#1E90FF", fg="white",
                                  font=("Helvetica", 12, "bold"), relief=tk.FLAT, command=self.processar_pagamentos)
        processar_btn.grid(row=0, column=1, padx=10)

        # Inicializa o estado dos campos
        self.atualizar_campos()

    def create_label_entry(self, parent, text, var, row, col):
        label = tk.Label(parent, text=text, font=("Helvetica", 12), bg="#f5f5f5")
        label.grid(row=row, column=col, padx=10, pady=5, sticky=tk.W)
        entry = tk.Entry(parent, textvariable=var, font=("Helvetica", 12), relief=tk.FLAT, bd=2)
        entry.grid(row=row, column=col + 1, padx=10, pady=5)
        return entry



    def atualizar_campos(self, event=None):
        tipo = self.tipo_funcionario_var.get()
        # Desabilitar ou habilitar campos com base no tipo de funcionário selecionado
        if tipo == "Comissário":
            self.set_entry_state(self.salario_entry, "normal")
            self.set_entry_state(self.comissao_entry, "normal")
            self.set_entry_state(self.total_vendas_entry, "normal")
            self.set_entry_state(self.valor_hora_entry, "disabled")
            self.set_entry_state(self.horas_dia_entry, "disabled")
        elif tipo == "Horalista":
            self.set_entry_state(self.salario_entry, "disabled")
            self.set_entry_state(self.comissao_entry, "disabled")
            self.set_entry_state(self.total_vendas_entry, "disabled")
            self.set_entry_state(self.valor_hora_entry, "normal")
            self.set_entry_state(self.horas_dia_entry, "normal")
        else:  # Mensalista
            self.set_entry_state(self.salario_entry, "normal")
            self.set_entry_state(self.comissao_entry, "disabled")
            self.set_entry_state(self.total_vendas_entry, "disabled")
            self.set_entry_state(self.valor_hora_entry, "disabled")
            self.set_entry_state(self.horas_dia_entry, "disabled")

    def set_entry_state(self, entry, state):
        entry.config(state=state)

    def get_float_value(self, var, default=0.0):
        try:
            # Substitui vírgula por ponto para tratar entradas no padrão BR
            value = float(var.get().replace(",", ".").strip())
            return value if value > 0 else default
        except ValueError:
            return default

    
    def limpar_campos(self):
        self.nome_var.set("")
        self.matricula_var.set("")
        self.num_proj_var.set("")
        self.salario_var.set("")
        self.comissao_var.set("")
        self.total_vendas_var.set("")
        self.valor_hora_var.set("")
        self.horas_dia_var.set("")
        self.tipo_funcionario_var.set("Mensalista")
        self.atualizar_campos()

    def cadastrar_funcionario(self):
        try:
            nome = self.nome_var.get()
            matricula = self.matricula_var.get().strip()
            num_proj = int(self.num_proj_var.get()) if self.num_proj_var.get().strip() else 0
            
            tipo = self.tipo_funcionario_var.get()
            if tipo == "Comissário":
                salario_base = self.get_float_value(self.salario_var)
                comissao = self.get_float_value(self.comissao_var) 
                total_vendas = self.get_float_value(self.total_vendas_var)
                funcionario = FuncionarioComissario(nome, matricula, num_proj, salario_base, comissao, total_vendas)
                salario_total = calcular_salario(funcionario)

            elif tipo == "Horalista":
                valor_hora = self.get_float_value(self.valor_hora_var)
                horas_dia = self.get_float_value(self.horas_dia_var)
                funcionario = FuncionarioHoralista(nome, matricula, num_proj, valor_hora, horas_dia)
                salario_total = calcular_salario(funcionario)

            else:  # Mensalista
                salario_base = self.get_float_value(self.salario_var)
                funcionario = FuncionarioMensalista(nome, matricula, num_proj, salario_base)
                salario_total = calcular_salario(funcionario)

            funcionario.salário_Total = salario_total
            self.funcionarios.append(funcionario)
            self.salvar_funcionario(funcionario)
            self.limpar_campos()

            messagebox.showinfo("Sucesso", f"Funcionário cadastrado com sucesso! ")

        except ValueError as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar funcionário: {str(e)}")

    def salvar_funcionario(self, funcionario):
        data = {
            "nome": funcionario.nome,
            "matricula": funcionario.matricula,
            "numero_de_projetos": funcionario.numero_de_projetos,
            "salario_base": getattr(funcionario, 'salario_base', None),
            "comissao": getattr(funcionario, 'comissao', None),
            "total_vendas": getattr(funcionario, 'total_vendas', None),
            "valor_por_hora": getattr(funcionario, 'valor_por_hora', None),
            "horas_por_dia": getattr(funcionario, 'horas_por_dia', None),
            "salário_Total": funcionario.salário_Total
        }

        try:
            with open('funcionarios.json', 'a') as f:
                f.write(json.dumps(data) + '\n')
        except IOError as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {str(e)}")
    
    def processar_pagamentos(self):
        try:
            with open('funcionarios.json', 'r') as f:
                funcionarios_data = [json.loads(line) for line in f]

            dados_excel = []
            resultado = ""

            for data in funcionarios_data:
                nome = data.get("nome")
                # Identifica o tipo de funcionário com base nos atributos exclusivos
                if data.get("comissao") is not None:
                    tipo = "Comissário"
                elif data.get("valor_por_hora") is not None:
                    tipo = "Horalista"
                else:
                    tipo = "Mensalista"

                salario = data.get("salário_Total", "N/A")
                numero_de_projetos = data.get("numero_de_projetos", 0)

                # Formata o salário para exibição
                salario_formatado = f"R$ {salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

                # Adiciona os dados na planilha Excel
                dados_excel.append({
                    "Nome": nome,
                    "Tipo": tipo,
                    "Salário Total": salario_formatado,
                    "Tem Projetos": "Sim" if numero_de_projetos > 0 else "Não"
                })

                # Adiciona ao resultado que será exibido na mensagem
                resultado += (
                    f"Funcionário: {nome}\n"
                    f"Tipo: {tipo}\n"
                    f"Salário: {salario_formatado}\n"
                    f"Tem Projetos: {'Sim' if numero_de_projetos > 0 else 'Não'}\n"
                    f"{'-'*50}\n"
                )

            # Cria o DataFrame e salva no Excel
            df = pd.DataFrame(dados_excel)
            df.to_excel("pagamentos_realizados.xlsx", index=False)

            # Mostra uma mensagem com os resultados resumidos
            messagebox.showinfo("Pagamentos", resultado)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar pagamentos: {str(e)}")



if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = App(root)
    root.mainloop()
