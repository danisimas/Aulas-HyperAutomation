class SaldoInsuficienteError(Exception):
    pass

class LimiteExcedidoError(Exception):
    pass

class ContaDestinoInvalidaError(Exception):
    pass

class ContaCorrente:
    def __init__(self, numero, titular, saldo_inicial, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite_transferencia = limite
        self.transacoes = []

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        
        if valor > self.limite_transferencia:
            raise LimiteExcedidoError("Limite de saque excedido.")
        
        self.saldo -= valor
        self.transacoes.append(f"Saque de R$ {valor}")

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f"Depósito de R$ {valor}")

    def transferir(self, valor, conta_destino):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
        
        if valor > self.limite_transferencia:
            raise LimiteExcedidoError("Limite de transferência excedido.")
        
        if conta_destino is None:
            raise ContaDestinoInvalidaError("Conta destino inválida.")
        
        self.sacar(valor)
        conta_destino.depositar(valor)
        self.transacoes.append(f"Transferência de R$ {valor} para a conta {conta_destino.numero}")
        conta_destino.transacoes.append(f"Transferência de R$ {valor} recebida da conta {self.numero}")

    def ver_extrato(self):
        print(f"Extrato da conta {self.numero} - Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo}")
        print("Transações:")
        for transacao in self.transacoes:
            print(transacao)

    def imprimir_dados(self):
        print(f"Conta {self.numero} - Titular: {self.titular}")
        print(f"Saldo: R$ {self.saldo}")
        print(f"Limite de transferência: R$ {self.limite_transferencia}")
        print("Transações:")
        for transacao in self.transacoes:
            print(transacao)

# Criação de contas
conta1 = ContaCorrente(12345, "João", 1000, 500)
conta2 = ContaCorrente(67890, "Maria", 0, 500)

# Transferência
conta1.transferir(200, conta2)

# Extrato e dados das contas
conta1.ver_extrato()
conta2.ver_extrato()
conta1.imprimir_dados()
conta2.imprimir_dados()

try:
    conta1.sacar(1200)  # Valor maior que o saldo (1000)
except SaldoInsuficienteError as e:
    print(e)  # Exibe "Saldo insuficiente."

# Exemplo 2: Disparando LimiteExcedidoError
try:
    conta1.sacar(600)  # Valor maior que o limite de saque (500)
except LimiteExcedidoError as e:
    print(e)  # Exibe "Limite de saque excedido."

# Exemplo 3: Disparando ContaDestinoInvalidaError
try:
    conta1.transferir(100, None)  # Conta destino é inválida (None)
except ContaDestinoInvalidaError as e:
    print(e)  # Exibe "Conta destino inválida."

# Exemplo 4: Disparando SaldoInsuficienteError em uma transferência
try:
    conta1.transferir(1500, conta2)  # Valor maior que o saldo disponível
except SaldoInsuficienteError as e:
    print(e)  # Exibe "Saldo insuficiente."

# Exemplo 5: Disparando LimiteExcedidoError em uma transferência
try:
    conta1.transferir(600, conta2)  # Valor maior que o limite de transferência
except LimiteExcedidoError as e:
    print(e)  # Exibe "Limite de transferência excedido."
