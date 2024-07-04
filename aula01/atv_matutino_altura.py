nome = input("Insira seu nome: ")

altura = float(input("Digite sua altura: "))


print(f"A altura de {nome} é {altura} cm")

print("A altura de %s é %.2f" %(nome, altura))


print("A altura de {:s} é {:.2f}".format(nome,altura))
