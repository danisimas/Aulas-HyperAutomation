import Livro
class Livraria:
    livros : Livro

    def __init__(self) -> None:
        self.livros = []

    def adicionar_livro(self):
        livro = Livro()
        livro