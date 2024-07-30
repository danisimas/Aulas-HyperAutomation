import os 
def arquivo ():
    if (os.path.isfile("exemplo.txt")):
        arq = open("exemplo.txt", "r")
        # arq.write("Estou escrevendo num arquivo po python")
        texto = arq.read()
        print(f"Conteúdo do arquivo: {texto}")

        arq.close()
    else:
        arq = open("exemplo.txt", "x")
        arq.close()


arquivo()