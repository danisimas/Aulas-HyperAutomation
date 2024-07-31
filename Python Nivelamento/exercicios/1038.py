n,quant = input().split()
n = int(n)
quant=int(quant)
if n ==1:
    valor = float(quant*4.00)
elif n ==2:
    valor = float(quant*4.50)
elif n ==3 :
        valor = float(quant*5.00)
elif n==4 :
    valor = float(quant*2.00)
else:
    valor = float(quant*1.50)
print("Total: R$ %.2f"%valor)
