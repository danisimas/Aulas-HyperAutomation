class IMC:
    nome = ''
    peso = 0.0
    altura = 0.0 
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura
    
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc
    
    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 16:
            return 'Magreza severa'
        elif imc < 16.9:
            return 'Magreza moderada'
        elif imc < 18.5:
            return 'Magreza leve'
        elif 18.5 <= imc < 25:
            return 'Peso ideal'
        elif 25 <= imc < 30:
            return 'Sobrepeso'
        elif 30 <= imc < 35:
            return 'Obesidade grau I'
        elif 35 <= imc < 40:
            return 'Obesidade grau II'
        else:
            return 'Obesidade grau III (severa)'

if __name__ == '__main__':
    pessoa = input("Nome: ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    
    pessoa = IMC(pessoa, peso, altura)

    print(f'{pessoa.nome} tem IMC {pessoa.calcular_imc():.2f} e classifica-se como {pessoa.classificar_imc()}')