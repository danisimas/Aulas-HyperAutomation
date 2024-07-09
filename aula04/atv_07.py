valores = [int(input("Digite os números: ")) for valores in range(10)]

numeros_pares = []

for vetor in valores:
    if vetor % 2 == 0:
        numeros_pares.append(vetor)
    

print(f"Vetor digitado:{valores}")


print(f"Números pares digitados:{numeros_pares}")
