N = int(input())
cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco= 0
dois = 0
um = 0
A=N
if int(N/100)>=0:
    cem = int(N / 100)
    N -=cem*100
if int(N/50)>=0:
    cinquenta = int(N/50)
    N -= cinquenta*50
if int(N/20)>=0:
    vinte = int(N/20)
    N -= vinte*20
if int(N/10)>=0:
    dez = int(N/10)
    N -= dez *10
if int(N/5)>=0:
    cinco = int(N/5)
    N -=cinco *5
if int(N/2)>=0:
    dois = int(N/2)
    N -=dois*2
if int(N/1)>=0:
    um = int(N/1)
    N -= um*1
print(A)
print("%d nota(s) de R$ 100,00" %cem)
print("%d nota(s) de R$ 50,00" %cinquenta)
print("%d nota(s) de R$ 20,00" %vinte)
print("%d nota(s) de R$ 10,00" %dez)
print("%d nota(s) de R$ 5,00" %cinco)
print("%d nota(s) de R$ 2,00" %dois)
print("%d nota(s) de R$ 1,00" %um)