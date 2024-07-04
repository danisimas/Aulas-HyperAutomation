numeros = input().split()
numeros_int = map(int,numeros)
for i in sorted(numeros_int):
     print(i)

print('')

for n in numeros:
    print(n)