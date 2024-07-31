d = int(input())
ano = d //365
d -= ano*365
mes = d//30
d-= mes *30
print("%d ano(s)\n%d mes(es)\n%d dia(s)"%(ano,mes,d))
