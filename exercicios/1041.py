coord1,coord2 = input().split()
coord1 = float(coord1)
coord2 = float(coord2)

if coord1 == 0 :
    print("Origem" if coord2 == 0 else 'Eixo Y' )
elif coord2 == 0:
    print("Eixo X")
elif coord1 > 0:
    print('Q1' if coord2 > 0 else 'Q4')
else:
    print('Q2' if coord2 > 0  else 'Q3')