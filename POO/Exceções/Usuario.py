class Usuario():
    def __init__(self, nome, email, idade):
        if nome is None or nome.strip() == "":
            raise ValueError("Nome não pode ser vazio.")
        
        if '@' not in email:
            raise ValueError("Email inválido.")
        
        if not isinstance(idade, int):
            raise TypeError("Idade precisa ser um número inteiro.")
        
        # Se todas as verificações passarem, os atributos são atribuídos
        self.nome = nome
        self.email = email
        self.idade = idade
    

try:
    pessoa_invalida_nome = Usuario("", "maria@example.com", 30)
except ValueError as e:
    print("Erro:", e)  # Exibe "Nome não pode ser vazio."

# Exemplo com email inválido
try:
    pessoa_invalida_email = Usuario("Maria", "mariaexample.com", 30)
except ValueError as e:
    print("Erro:", e)  # Exibe "Email inválido."

# Exemplo com idade não inteira
try:
    pessoa_invalida_idade = Usuario("Carlos", "carlos@example.com", "trinta")
except TypeError as e:
    print("Erro:", e)  # Exibe "Idade precisa ser um número inteiro."