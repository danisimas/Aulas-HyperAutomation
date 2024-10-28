class Autor:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros = []
    
    def adicionar_livro(self, livro):
        self.__livros.append(livro)
    
    def mostrar_livros(self):
        for livro in self.__livros:
            print(livro.get_titulo())
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_livros(self):
        return self.__livros
