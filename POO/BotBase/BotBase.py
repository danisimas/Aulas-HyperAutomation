class BotBase:
    def preencher(self):
        pass


class BotCadastro(BotBase):
    
    def __init__(self, nome, email, senha) -> None:
        super().__init__()
        self.nome = nome
        self.email = email
        self.senha = senha

    def preencher(self):
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')
        print(f'Senha: {self.senha}')


class BotAtualizacao(BotBase):
    
    def __init__(self, nome, email, senha, novo_email, nova_senha) -> None:
        super().__init__()
        self.nome = nome
        self.email = email
        self.senha = senha
        self.novo_email = novo_email
        self.nova_senha = nova_senha
    
    def preencher(self):
        print(f'Nome: {self.nome}')
        print(f'Email: {self.email}')
        print(f'Senha: {self.senha}')
        print(f'Novo Email: {self.novo_email}')
        print(f'Nova Senha: {self.nova_senha}')


def processar_formulario(bot: BotBase):
    bot.preencher()


if __name__ == '__main__':
    bot_cadastro = BotCadastro('John Doe', 'johndoe@example.com', 'password123')
    processar_formulario(bot_cadastro)
    
    bot_atualizacao = BotAtualizacao('John Doe', 'johndoe@example.com', 'password123', 'newemail@example.com', 'newpassword456')
    processar_formulario(bot_atualizacao)
