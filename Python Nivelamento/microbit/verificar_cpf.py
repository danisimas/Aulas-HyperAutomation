from microbit import *
import radio

radio.config(group=53)
radio.on()

cpfs_validos = []
cpfs_invalidos = []
cpf = 0

def enviar_cpf():
    cpf = input("Digite seu CPF ou parar para finalizar: ")
    return cpf

def exibir_contagem():
    display.scroll("Validos: " + str(len(cpfs_validos)))
    display.scroll("Invalidos: " + str(len(cpfs_invalidos)))

def receber_cpf(cpf, valido):
    if len(cpf)==0:
        pass
    if len(cpf)!=0 and valido=='valido':
        display.scroll("Valido")
        cpfs_validos.append((cpf, "Valido"))
    else:
        display.scroll("Invalido")
        cpfs_invalidos.append((cpf, "Invalido"))

while True:
    if button_a.was_pressed():
        cpf_enviar = enviar_cpf()
        if cpf_enviar.lower() == "parar":
            exibir_contagem()
        radio.send(cpf_enviar)
        cpf = cpf_enviar
    if button_b.was_pressed():
        valido = radio.receive()
        receber_cpf(cpf,valido)
    if accelerometer.was_gesture('shake'):
        break
        
def verificacao(cpf):

    def calcular_digito(cpf_s, peso):
        soma = 0

        for i, digito in enumerate(cpf_s):
            soma += int(digito) * peso
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
           radio.send('valido')
       else:
           radio.send('invalido')