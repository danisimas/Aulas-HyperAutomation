def soma (num1, num2):
    total = num1 + num2
    return total

def subtracao (num1, num2):
    if(num1 < num2):
        num2, num1 = num1, num2
    total = num1 - num2
    return total


while True:
    print("""\nMenu:
1. Somar
2. Subtrair
3. Sair\n
""")
    operacao = int(input("Escolha uma opção: "))

    match(operacao):
        case 1:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Soma:", soma(num1, num2))     
        case 2:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Subtração:", subtracao(num1, num2))  
        case 3:
            break