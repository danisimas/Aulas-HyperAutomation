class Livro:
    def __init__(self, titulo, autor, codigo):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = codigo
        self.__disponivel = True
        autor.adicionar_livro(self)
    
    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
        else:
            print(f"O livro '{self.__titulo}' já está emprestado.")
    
    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
        else:
            print(f"O livro '{self.__titulo}' já está disponível.")
    
    # Getters e setters
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def is_disponivel(self):
        return self.__disponivel
