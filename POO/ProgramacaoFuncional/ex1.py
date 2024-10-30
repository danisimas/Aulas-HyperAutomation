from functools import reduce

class Venda:
    def __init__(self, nome_produto, quantidade, preco_unitario):
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    @property
    def total(self):
        return self.quantidade * self.preco_unitario


# Classe HistoricoVendas
class HistoricoVendas:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    def total_por_produto(self):
        # Usando reduce para calcular o total por produto
        totais = {}
        for venda in self.vendas:
            totais[venda.nome_produto] = reduce(
                lambda acc, v: acc + (v.total if v.nome_produto == venda.nome_produto else 0),
                self.vendas, 
                0
            )
        return totais

    def listar_vendas_acima_de(self, valor):
        for venda in self.vendas:
            if venda.total > valor:
                yield venda


# Classe Funcionario
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario


# Decorator para autenticar acesso
def autenticar_acesso(func):
    def wrapper(self, solicitante, *args, **kwargs):
        if solicitante.cargo == "Gerente":
            return func(self, solicitante, *args, **kwargs)
        else:
            raise PermissionError("Acesso negado. Somente gerentes podem aumentar salários.")
    return wrapper


# Classe SistemaRH
class SistemaRH:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    @autenticar_acesso
    def aumentar_salario(self, solicitante, funcionario, percentual):
        funcionario.salario += funcionario.salario * percentual / 100


# Classe Conta
class Conta:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor):
        self.transacoes.append({"tipo": tipo, "valor": valor})

    def filtrar_transacoes_por_tipo(self, tipo):
        return list(filter(lambda transacao: transacao["tipo"] == tipo, self.transacoes))

    def aplicar_taxa(self, taxa):
        def aplicar_taxa_saque(transacao):
            if transacao["tipo"] == "Saque":
                transacao["valor"] -= transacao["valor"] * taxa
            return transacao

        self.transacoes = list(map(aplicar_taxa_saque, self.transacoes))


if __name__ == "__main__":
    # Exemplo com HistoricoVendas
    venda1 = Venda("Pão", 10, 1.50)
    venda2 = Venda("Café", 5, 3.00)
    venda3 = Venda("Batata", 15, 0.75)
    historico_vendas = HistoricoVendas()
    historico_vendas.adicionar_venda(venda1)
    historico_vendas.adicionar_venda(venda2)
    historico_vendas.adicionar_venda(venda3)
    print(historico_vendas.total_por_produto())

    for venda in historico_vendas.listar_vendas_acima_de(10):
        print(f"Venda: {venda.nome_produto} - Total: R$ {venda.total:.2f}")
    
    # Exemplo com SistemaRH e Funcionario
    gerente = Funcionario("Gerente", "Gerente", 5000)
    funcionario = Funcionario("Maria", "Analista", 3000)
    
    sistema_rh = SistemaRH()
    sistema_rh.adicionar_funcionario(gerente)
    sistema_rh.adicionar_funcionario(funcionario)

    sistema_rh.aumentar_salario(gerente, funcionario, 10)
    print(f"Novo salário de {funcionario.nome}: R$ {funcionario.salario:.2f}")
    
    # Exemplo com Conta
    conta = Conta()
    conta.adicionar_transacao("Saque", 1000)
    conta.adicionar_transacao("Saque", 2000)
    conta.adicionar_transacao("Deposito", 3000)
    print(conta.filtrar_transacoes_por_tipo("Saque"))

    conta.aplicar_taxa(0.05)
    print(conta.transacoes)
