class Pessoa:
    nome = ''
    idade = 0
    peso = 0.0
    altura = 0.0
    
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def calcular_crescimento(self, idade):
        if self.idade >= 21:
            return None
        if self.idade < 21: 
            return self.altura * 0.05
    def envelhecer(self, idade):
        self.idade += 1
        self.peso += 0.01
        self.altura += 0.005
        print ("Esta ficando velho")
    
    def engordar(self, peso):
        self.peso += peso
        print ("Esta ficando mais gordo")
    
    def emagrecer(self, peso):
        self.peso -= peso
        print ("Esta ficando mais magro")


if __name__ == '__main__':
    pessoa = input("Nome: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))

    p = Pessoa(pessoa, idade, peso, altura)
    crescimento = p.calcular_crescimento(idade)
    p.envelhecer(idade)
    p.engordar(10)
    p.emagrecer(5)
    
    print(f"Nome: {p.nome}")
    
    if crescimento is None:
        print(f"{pessoa}, Você parou de crescer")
    else:
        print(f"{pessoa}, o crescimento é de {crescimento:.2f} centimetros.")
    