soma_dos_valores = 0
quantidade_positivos = 0
quantidade_negativos = 0

while True:
    valor = float(input("Digite um valor (ou 0 para encerrar): "))
    if valor == 0:
        break
    if valor > 0:
        quantidade_positivos += 1
    elif valor < 0:
        quantidade_negativos += 1
    soma_dos_valores += valor

if quantidade_positivos + quantidade_negativos > 0:
    media = soma_dos_valores / (quantidade_positivos + quantidade_negativos)
    percentual_positivos = (quantidade_positivos / (quantidade_positivos + quantidade_negativos)) * 100
    percentual_negativos = (quantidade_negativos / (quantidade_positivos + quantidade_negativos)) * 100

    print(f"Média aritmética dos valores: {media:.2f}")
    print(f"Quantidade de valores positivos: {quantidade_positivos}")
    print(f"Quantidade de valores negativos: {quantidade_negativos}")
    print(f"Percentual de valores positivos: {percentual_positivos:.2f}%")
    print(f"Percentual de valores negativos: {percentual_negativos:.2f}%")
else:
    print("Nenhum valor válido foi inserido.")
