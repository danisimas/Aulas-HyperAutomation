# Imports go at the top
from microbit import *


import radio
radio.config(group=53)
radio.on()

def verificacao(cpf):

    def calcular_digito(cpf_s, peso):
        soma = 0

        for i, digito in enumerate(cpf_s):
            soma += int(digito) * peso
            print(digito)
            peso += 1
            
        digito = soma % 11

        return digito if digito < 10 else 0

    cpf_string = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf_string)!=11 or cpf_string == cpf_string[0]*11:
        return False
    else:
        digito1 = calcular_digito(cpf_string[:9], 1)
        digito2 = calcular_digito(cpf_string[:10], 0)

    if cpf_string[-2:] == "{}{}".format(digito1, digito2):
        return True
        

while True:
    cpf = radio.receive()
    if cpf:
       if verificacao(cpf):
           radio.send('Valido')
       else:
           radio.send("Invalido")



from microbit import *
import radio

radio.config(group=53)
radio.on()

cpfs_validos = []
cpfs_invalidos = []

def enviar_cpf():
    cpf = input("Digite seu CPF: ")
    return cpf

def receber_cpf(cpf,valido):
    if valido=='Valido':
        display.scroll("Valido")
        cpfs_validos.append((cpf, "Valido"))
    else:
        display.scroll("Invalido")
        cpfs_invalidos.append((cpf, "Invalido"))

while True:
    cpf_enviar = enviar_cpf()
    radio.send(cpf_enviar)
    valido = radio.receive()
    receber_cpf(cpf_enviar, valido)
