class Livro():
    def __init__(self, titulo, autor, id, disponivel=True):
        self.titulo = titulo
        self.autor = []
        self.id = id
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'Livro "{self.titulo}" emprestado com sucesso.')
        else:
            print(f'Livro "{self.titulo}" não está disponível.')
    
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'Livro "{self.titulo}" devolvido com sucesso.')
        else:
            print(f'Livro "{self.titulo}" já está disponível.')
    
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, novo_titulo):
        if novo_titulo:
            self._titulo = novo_titulo
        else:
            print('Título inválido.')
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        if novo_id and isinstance(novo_id, int):
            self._id = novo_id
        else:
            print('ID inválido.')
    
    @property
    def disponivel(self):
        return self._disponivel
    
    @disponivel.setter
    def disponivel(self, novo_disponivel):
        if isinstance(novo_disponivel, bool):
            self._disponivel = novo_disponivel
        else:
            print('Disponibilidade inválida.')
    
class Autor():
    def __init__(self, nome, livros):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self):
        titulo = input("Insira o título do livro: ")
        id = int(input("Insira o ID do livro: "))
        novo_livro = Livro(titulo, self.nome, id)
        self.livros.append(novo_livro)
    
    def listar_livros(self):
        for livro in self.livros:
            print(f"ID: {livro.id}, Título: {livro.titulo}")
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if novo_nome:
            self._nome = novo_nome
        else:
            print('Nome inválido.')
    
    @property
    def livros(self):
        return self._livros
    
    @livros.setter
    def livros(self, novos_livros):
        if isinstance(novos_livros, list):
            self._livros = novos_livros
        else:
            print('Livros inválidos.')

