import json
import pickle
from functools import wraps

import Pedido

# Decorator para log de atividades
def log_atividade(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Método: {func.__name__}, Args: {args[1:]}, Retorno: {result}")
        return result
    return wrapper

class GestorDePedidos:
    def __init__(self):
        self.pedidos = []

    @log_atividade
    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    @log_atividade
    def listar_pedidos_por_status(self, status):
        return list(filter(lambda p: p.status == status, self.pedidos))

    def pedidos_por_categoria(self, categoria):
        return sum(
            self.quantidade[produto]
            for pedido in self.pedidos
            for produto in pedido.produtos
            if produto.categoria == categoria
        )

    def total_vendas(self):
        return sum(pedido.total_pedido() for pedido in self.pedidos)

    # Manipulação de arquivos
    def salvar_dados_json(self, filename="pedidos.json"):
        try:
            with open(filename, "w") as f:
                json.dump([pedido.__dict__ for pedido in self.pedidos], f)
        except Exception as e:
            print(f"Erro ao salvar dados em JSON: {e}")

    def carregar_dados_json(self, filename="pedidos.json"):
        try:
            with open(filename, "r") as f:
                pedidos_data = json.load(f)
                self.pedidos = [Pedido(**data) for data in pedidos_data]
        except FileNotFoundError:
            print("Arquivo JSON não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar dados do JSON: {e}")

    def salvar_dados_binario(self, filename="pedidos.pkl"):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self.pedidos, f)
        except Exception as e:
            print(f"Erro ao salvar dados em binário: {e}")

    def carregar_dados_binario(self, filename="pedidos.pkl"):
        try:
            with open(filename, "rb") as f:
                self.pedidos = pickle.load(f)
        except FileNotFoundError:
            print("Arquivo binário não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar dados do binário: {e}")
