A , B , C , D = input().split()

A = int(A)
B = int(B)
C = int(C)
D = int(D)

total_minutos_inicial = A * 60 + B
total_minutos_final = C * 60 + D

diferenca_minutos = total_minutos_final - total_minutos_inicial

if diferenca_minutos < 0:
    diferenca_minutos += 24 * 60

if diferenca_minutos == 0 and (A == C and B == D):
    diferenca_minutos = 24 * 60

horas_falt = diferenca_minutos // 60 
minutos_falt = diferenca_minutos % 60

print(f"O JOGO DUROU {horas_falt} HORA(S) E {minutos_falt} MINUTO(S)")
