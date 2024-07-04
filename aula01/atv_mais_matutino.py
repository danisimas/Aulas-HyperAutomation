

# Exercicio 1

dimensao_base = float(input("Digite a base do terreno \n"))
dimensao_altura = float(input("Digite a altura do terreno \n"))

area_terreno = dimensao_base * dimensao_altura

print(f"Area do terreno é  {area_terreno}\n")


# Exercicio 2

quant_cavalos = int(input("Digite a quantidade de cavalos que você tem \n" ))

quant_ferraduras = quant_cavalos * 4

print(f"A Quantidade de ferraduras para a quantidade {quant_cavalos} de cavalos é {quant_ferraduras} \n ")


# Exercicio 3

quant_paes = int(input("Insira a quantidade pães vendidos hoje \n"))
quant_broas = int(input("Insira a quantidade broas vendidos hoje \n"))


total_arrecado = (quant_paes * 0.12) + (quant_broas * 1.50)

poupanca = total_arrecado * 0.1


print(f"Total arecadado: {total_arrecado} \n")
print(f"Poupança: {poupanca} \n")



# Exercicio 4

nome = input("Digite seu nome \n")
idade = int(input("Digite sua idade\n"))

dias = idade * 365

print(f"{nome} JÁ VIVEU {dias} DIAS\n ")


# Exercicio 5

dinheiro = float(input("Digite o valor em R$: "))

preco_litro = float(input("Digite o preço da gasolina: "))

quant_litros = dinheiro/preco_litro

print(f"Litros: {quant_litros} \n")


# Exercicio 6

peso_comida = int(input("Valor do peso \n"))

valor_pagar = peso_comida * 12

print(f"Valor a pagar: {valor_pagar}\n")


# Exercicio 7

dia = int(input("Dia:"))
mes = int(input("Mes:"))

quant_dias = (dia + mes ) * 30

print(f"Ja se passaram {quant_dias} dias \n")



# Exercicio 8

nota1 = int(input("Digite o valor das notas \n"))
nota2 = int(input("Digite o valor das notas \n"))
nota3 = int(input("Digite o valor das notas \n"))

media = (nota1*1) + (nota2*2) + (nota3*3) / 6

print(f"Média: {media} \n")



# Exercicio 9
tam10_quant = int(input("Quantidade de blusas pequenas \n"))
tam12_quant = int(input("Quantidade de blusas médias \n"))
tam15_quant = int(input("Quantidade de blusas grandes \n"))

valor_arrecadado = (tam10_quant * 10) + (tam12_quant * 12) + (tam15_quant * 15)

print(f"Valor Total: {valor_arrecadado} \n")

# Exercicio 10
altura = float(input("Digite sua altura \n"))
peso = float(input("Digite seu peso \n"))

imc = peso / (altura * altura)

print(f"IMC: {imc} \n")
