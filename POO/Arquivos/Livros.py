import json
import csv
import pickle
from functools import reduce

# Classe Livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

    
    

    
    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', ano_publicacao={self.ano_publicacao}, genero='{self.genero}')"


# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def listar_livros_por_autor(self, autor):
        return list(filter(lambda livro: livro.autor == autor, self.livros))
    
    def contar_livros_por_genero(self, genero):
        return reduce(lambda acc, livro: acc + 1 if livro.genero == genero else acc, self.livros, 0)
    
    def listar_titulos(self):
        return list(map(lambda livro: livro.titulo, self.livros))
    
    def exportar_dados(self, formato):
        if formato == 'texto':
            with open("biblioteca.txt", "w") as file:
                for livro in self.livros:
                    file.write(f"{livro.titulo},{livro.autor},{livro.ano_publicacao},{livro.genero}\n")
        elif formato == 'json':
            with open("biblioteca.json", "w") as file:
                json.dump([livro.__dict__ for livro in self.livros], file)
        elif formato == 'csv':
            with open("biblioteca.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Titulo", "Autor", "Ano Publicacao", "Genero"])
                for livro in self.livros:
                    writer.writerow([livro.titulo, livro.autor, livro.ano_publicacao, livro.genero])
        elif formato == 'binario':
            with open("biblioteca.pkl", "wb") as file:
                pickle.dump(self.livros, file)
    
    def importar_dados(self, formato):
        if formato == 'texto':
            with open("biblioteca.txt", "r") as file:
                self.livros = [Livro(*line.strip().split(',')) for line in file]
        elif formato == 'json':
            with open("biblioteca.json", "r") as file:
                dados = json.load(file)
                self.livros = [Livro(**livro) for livro in dados]
        elif formato == 'csv':
            with open("biblioteca.csv", "r") as file:
                reader = csv.DictReader(file)
                self.livros = [Livro(row['Titulo'], row['Autor'], int(row['Ano Publicacao']), row['Genero']) for row in reader]
        elif formato == 'binario':
            with open("biblioteca.pkl", "rb") as file:
                self.livros = pickle.load(file)
    
    def filtrar_livros(self, ano=None, genero=None):
        return list(filter(lambda livro: (ano is None or livro.ano_publicacao == ano) and (genero is None or livro.genero == genero), self.livros))
    
    def realizar_backup(self):
        self.exportar_dados('binario')  # Backup em JSON


# Teste das funcionalidades

# Criando uma instância da biblioteca
biblioteca = Biblioteca()

# Adicionando novos livros
biblioteca.adicionar_livro(Livro("Livro A", "Autor 1", 2021, "Ficcao"))
biblioteca.adicionar_livro(Livro("Livro B", "Autor 2", 2020, "Aventura"))
biblioteca.adicionar_livro(Livro("Livro C", "Autor 1", 2019, "Ficcao"))
biblioteca.adicionar_livro(Livro("Livro D", "Autor 3", 2022, "Historia"))
biblioteca.adicionar_livro(Livro("Livro E", "Autor 2", 2021, "Fantasia"))

# Consultar livros por autor
print("Livros do Autor 1:", biblioteca.listar_livros_por_autor("Autor 1"))

# Contar livros por gênero
print("Total de livros de Ficcao:", biblioteca.contar_livros_por_genero("Ficcao"))

# Exportando e importando dados em diferentes formatos
biblioteca.exportar_dados("binario")
biblioteca.importar_dados("json")

# Verificar consistência dos dados após a importação
print("Livros importados:", biblioteca.livros)

# Relatório funcional: lista de títulos de todos os livros
print("Lista de títulos:", biblioteca.listar_titulos())

# Filtros funcionais avançados
print("Filtrando livros de Ficcao publicados em 2021:", biblioteca.filtrar_livros(ano=2021, genero="Ficcao"))

# Função de backup
biblioteca.realizar_backup()
