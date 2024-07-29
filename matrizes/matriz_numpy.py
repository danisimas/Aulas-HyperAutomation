import numpy as np

matriz = []

for i in range(6):
    num = int(input("Digite o números para uma matriz 3x3:"))
    matriz.append(num)

matriz_soma = np.sum(matriz)

matriz_transporta = np.transpose(matriz)

matriz_mult_transporta = np.dot(matriz_transporta,matriz)


print(f"Matriz original: {matriz}\n")
print(f"Matriz transporta: {matriz_transporta}\n")
print(f"Matriz soma: {matriz_soma}\n")
print(f"Matriz mult_transporta: {matriz_mult_transporta}\n")


matriz_quad = []

for i in range(8):
    num = int(input("Digite o números para uma matriz 3x3:"))
    matriz_quad.append(num)

matriz_quad_diagonal_principal = np.trace(matriz_quad)


print(f"Soma da Matriz quadrada diagonal principal: {matriz_quad_diagonal_principal}\n")