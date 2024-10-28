class Biblioteca:
    total_livros = 0
    
    def __init__(self, nome):
        self.nome = nome
        self.__livros = []
        self.__emprestimos = {}
    
    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        Biblioteca.total_livros += 1
    
    def registrar_emprestimo(self, codigo_livro, cliente):
        for livro in self.__livros:
            if livro.get_codigo() == codigo_livro and livro.is_disponivel():
                livro.emprestar()
                self.__emprestimos[codigo_livro] = cliente
                print(f"Empréstimo registrado: {livro.get_titulo()} para {cliente}.")
                return
        print(f"Livro com código {codigo_livro} não disponível para empréstimo.")
    
    def registrar_devolucao(self, codigo_livro):
        if codigo_livro in self.__emprestimos:
            for livro in self.__livros:
                if livro.get_codigo() == codigo_livro:
                    livro.devolver()
                    del self.__emprestimos[codigo_livro]
                    print(f"Devolução registrada: {livro.get_titulo()}.")
                    return
        print(f"Livro com código {codigo_livro} não está emprestado.")
    
    def mostrar_livros_disponiveis(self):
        print("Livros disponíveis:")
        for livro in self.__livros:
            if livro.is_disponivel():
                print(f"{livro.get_titulo()} (Código: {livro.get_codigo()})")
    
    @classmethod
    def mostrar_total_livros(cls):
        print(f"Total de livros na biblioteca: {cls.total_livros}")

