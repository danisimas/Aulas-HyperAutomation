# Team Phoenix: Marielle, Daniele, Carlos e Luiz

numeros = []

while True:
    print("""\nMenu:
1. Adicionar um número
2. Remover um número
3. Exibir o vetor completo
4. Encontrar e exibir o maior e o menor número
5. Calcular e exibir a soma de todos os números
6. Sair\n
""")
    operacao = int(input("Escolha uma opção: "))

    match(operacao):
        case 1:
            num = int(input("Digite o número para adicionar: "))
            numeros.append(num)
        case 2:
            if (len(numeros)==0):
                print("Impossível remover número\n")
            else:
                rmv = int(input("Digite o número para remover: "))
                numeros.remove(rmv)
        case 3:
            print(numeros)
        case 4:
            maximo = max(numeros)
            minimo = min(numeros)
            print(f"O maior número é {maximo}")
            print(f"O menor número é {minimo}")
        case 5:
            soma = 0

            for num in numeros:
                soma += num

            media = soma/(len(numeros))
            print(f"Média: {media}")

        case 6:
            break