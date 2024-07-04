ladoA = int(input("LADO A: \n"))
ladoB = int(input("LADO B: \n"))
ladoC = int(input("LADO C: \n"))

if ladoB+ladoA>ladoC and ladoC+ladoB> ladoA and ladoC+ladoA> ladoB:
    print("É um triângulo")
    if (ladoB==ladoA==ladoC):
        print ("Equilátero")
    elif (ladoB==ladoC or ladoC==ladoA or ladoA==ladoB):
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não é")