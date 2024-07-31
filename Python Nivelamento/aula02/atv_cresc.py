# exercicio 5 

menor = 0
maior = 0
medio = 0

num1 = int(input("Digite o valor dos numeros \n"))
num2 = int(input("Digite o valor dos numeros \n"))
num3 = int(input("Digite o valor dos numeros \n"))


if num1 == num2 == num3:
    print("Não é possivél fazer ordem crescente com números iguais")
else:
    if (num1>num2 and num1>num3):
            maior = num1
    elif (num1<num2 and num1< num3):
            menor = num1
    else:
           medio = num1
    
    if (num2>num1 and num2>num3):
            maior = num2
    elif (num2<num1 and num2<num3):
            menor = num2
    else:
           medio = num2       
    
    if (num3>num1 and num3>num2):
            maior = num3
    elif (num3<num1 and num3<num2):
            menor = num3
    else:
           medio = num3
    
print(f"ORDEM CRESCENTE: {menor} - {medio} - {maior}")