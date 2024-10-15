class Livro:
    titulo = ''
    autor = ''
    disponivel = True

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    
    @property
    def titulo(self):
        return self.titulo
    @titulo.setter
    def titulo(self, titulo):
        if self.titulo  is not None:
            raise ValueError('Título do livro não pode ser alterado')
        self.titulo = titulo
    
    @property
    def autor(self):
        return self.autor
    
    @autor.setter
    def autor(self, autor):
        if self.autor is not None:
            raise ValueError('Autor do livro não pode ser alterado')
        self.autor = autor
    
    @property
    def disponivel(self):
        return self.disponivel
    
    @disponivel.setter
    def disponivel(self, disponivel):
        if self.disponivel is not None:
            raise ValueError('Disponibilidade do livro não pode ser alterada')
        self.disponivel = disponivel

    @classmethod
    def emprestar(self, int):
        if self.disponivel:
            self.disponivel = False
            print(f'{self.titulo} emprestado por {int.nome}')
        else:
            print(f'{self.titulo} já está emprestado')
    @classmethod
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'{self.titulo} devolvido')
        else:
            print(f'{self.titulo} já está disponível')
    @classmethod
    def mostrar_info(self,int):
        print(f'Livro: {self.titulo}, Autor: {self.autor}, Emprestado por: {int.nome if not self.disponivel else "Livro não emprestado"}')