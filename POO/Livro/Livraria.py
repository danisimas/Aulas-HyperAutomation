class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'O livro "{self.titulo}" foi emprestado.')
        else:
            print(f'O livro "{self.titulo}" não está disponível no momento.')

    def devolver(self):
        self.disponivel = True
        print(f'O livro "{self.titulo}" foi devolvido e está disponível.')

    def mostrar_info(self):
        status = "disponível" if self.disponivel else "emprestado"
        print(f'Título: {self.titulo}, Autor: {self.autor}, Status: {status}')

class Livraria:

    def __init__(self):
        self.inventario = []

    def adicionar_livro(self, livro):
        self.inventario.append(livro)
        print(f'O livro "{livro.titulo}" foi adicionado ao inventário.')

    def emprestar_livro(self, titulo):
        for livro in self.inventario:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f'O livro "{titulo}" não foi encontrado no inventário.')

    def mostrar_inventario(self):
        if len(self.inventario) == 0:
            print("O inventário está vazio.")
        else:
            print("Inventário da Livraria:")
            for livro in self.inventario:
                livro.mostrar_info()

if __name__ == "__main__":
   
    livraria = Livraria()

    livro1 = Livro("1984", "George Orwell")
    livro2 = Livro("Dom Casmurro", "Machado de Assis")

    livraria.adicionar_livro(livro1)
    livraria.adicionar_livro(livro2)

  
    livraria.mostrar_inventario()

   
    livraria.emprestar_livro("1984")


    livraria.emprestar_livro("1984")

  
    livro1.devolver()

   
    livraria.mostrar_inventario()