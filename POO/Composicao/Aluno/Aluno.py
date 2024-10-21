class Aluno():
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def imprimir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matricula: {self.matricula}")


class Curso():
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []

    def adicionar_aluno(self):
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matricula do aluno: ")
        aluno = Aluno(nome, matricula)
        self.alunos.append(aluno)
    
    def imprimir_dados(self):
        print(f"Nome do curso: {self.nome}")
        print(f"Codigo do curso: {self.codigo}")
        print("Alunos:")
        for aluno in self.alunos:
            aluno.imprimir_dados()

class Escola():
    def __init__(self, nome):
        self.cursos = []
        self.nome = nome

    def adicionar_curso(self):
        nome = input("Digite o nome do curso: ")
        codigo = input("Digite o codigo do curso: ")
        curso = Curso(nome, codigo)
        self.cursos.append(curso)
    
    def imprimir_dados(self):
        print(f"Nome da escola: {self.nome}")
        print("Cursos:")
        for curso in self.cursos:
            curso.imprimir_dados()
    

if __name__ == "__main__":
    escola = Escola("Universidade Federal do Amazonas")
    escola.adicionar_curso()
    escola.imprimir_dados()
    escola.cursos[0].adicionar_aluno()
    escola.imprimir_dados()


'''
1. Como a composição facilita a criação de relações complexas entre
objetos?

R = A composição ajuda na relação de coesão aos objetos, dos quais não sofrem com a relação de herança de um objeto pai, assim podendo ter mais independencia de suas classes e métodos.

2. Qual é a vantagem de usar composição em vez de herança neste
exercício?

R = A vantagem de usar a composição é a coesão dos objetos e que cada classe como
Escola, Curso e Aluno não necessitam está dentro de uma herança

3. Como o encapsulamento é utilizado nas classes Aluno, Curso e Escola?
R = O encapsulamento é usado quando podemos já chamar a classe Escola dando os métodos e conseguimos já fazer a inserção
dos outros objetos

4. Como você pode estender este sistema para incluir novas
funcionalidades, como notas dos alunos e professores para cada curso?

R = Criaria uma classe Professor para adicionar nos cursos e uma classe Notas para ser independente dos Alunos




'''