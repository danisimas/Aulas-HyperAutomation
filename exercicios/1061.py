dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(" : "))
dia_fim = int(input().split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(" : "))

inicio_em_segundos = (dia_inicio * 24 * 3600) + (hora_inicio * 3600) + (minuto_inicio * 60) + segundo_inicio
fim_em_segundos = (dia_fim * 24 * 3600) + (hora_fim * 3600) + (minuto_fim * 60) + segundo_fim


duracao_em_segundos = fim_em_segundos - inicio_em_segundos


dias = duracao_em_segundos // (24 * 3600)
duracao_em_segundos %= 24 * 3600
horas = duracao_em_segundos // 3600
duracao_em_segundos %= 3600
minutos = duracao_em_segundos // 60
segundos = duracao_em_segundos % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
