
from Forms.FormContato import FormContato

class FormLogin(FormContato):
    def __init__(self, nome, email, password, telefone):
        super().__init__(nome, email, password, telefone)
    
    def login(self):
        if self.validar_email() and self.validar_senha() and self.validar_telefone():
            print("Login efetuado com sucesso!")
        else:
            print("Login inválido!")

    def imprimir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Telefone: {self.telefone}")