
num1, num2 = map(int,input("Números para a soma: ").split())
soma = 0 

if num1 > num2:   
        num1, num2 = num2, num1
for i in range(num1, num2+1,1):
 
    if ( i % 2 == 0 ):
        soma +=i

print(f"Soma: {soma}")