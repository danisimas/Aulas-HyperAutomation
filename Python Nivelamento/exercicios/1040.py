N1,N2,N3,N4 = input().split()
N1=float(N1)
N2=float(N2)
N3=float(N3)
N4=float(N4)
media =  (N1*2+N2*3+N3*4+N4*1) / (2+3+4+1)
if media >=7.0:
    print("Media: %.1f"%media)
    print("Aluno aprovado.")
elif media < 5.0:
    print("Media: %.1f"%media)
    print("Aluno reprovado.")
else:
    print("Media: %.1f"%media)
    print("Aluno em exame.")
    notaExame = float(input())
    print('Nota do exame: %.1f'%notaExame)
    mediaFinal = (media + notaExame)/2
    if mediaFinal>=5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f" %mediaFinal)