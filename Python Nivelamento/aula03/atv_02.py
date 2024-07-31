
maior_altura = float('-inf')  
menor_altura = float('inf')   

contador = 1  

while contador <= 15:  
    altura = float(input(f"Digite a altura da pessoa {contador}: "))
    while altura <= 0.0:
        print("Altura inválida! A altura deve ser maior que 0.")
        altura = float(input(f"Digite a altura da pessoa {contador}: "))
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
    contador += 1  

print(f"Maior altura: {maior_altura}")
print(f"Menor altura: {menor_altura}")
