
area = 0
lado = int(input("Digite a quantidade de lados:"))

if lado == 3:
    print("Triangulo")
    num1 = int(input("Digite os valores: \n"))
    num2 = int(input("Digite os valores: \n"))
    area = (num1 * num2) / 2 

    print(f"Area do triangulo: {area}\n")

elif lado == 4:
    print("Quadrado")
    num_quad = int(input("Digite os valores: \n"))  
    area  = num_quad **2
    print(f"Area do quadrado: {area}\n")

else:
    print("Pentagono")
    perimetro = int(input("Digite os valores: \n"))
    apotema = int(input("Digite os valores: \n"))
    area = perimetro * apotema
    print(f"Area do pentagono: {area}\n")
