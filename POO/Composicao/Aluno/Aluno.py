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
    escola = Escola("Universidade Federal de Minas Gerais")
    escola.adicionar_curso()
    escola.imprimir_dados()
    escola.cursos[0].adicionar_aluno()
    escola.imprimir_dados()
