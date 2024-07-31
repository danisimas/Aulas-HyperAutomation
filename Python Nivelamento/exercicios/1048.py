A = float(input())

salario_novo = 0
percentual_ganho = 0
reajuste = 0


if A <= 400.00:
    salario_novo = A * 1.15 
    percentual_ganho = 15 
    reajuste = salario_novo - A

elif 400.01 <= A <= 800.00:
    salario_novo = A * 1.12
    percentual_ganho = 12 
    reajuste = salario_novo - A 

      
elif 800.01 <= A <= 1200.00:
    salario_novo = A * 1.1
    percentual_ganho = 10
    reajuste = salario_novo - A
    

elif 1200.01 <= A <= 2000.00:
    salario_novo = A * 1.07
    percentual_ganho = 7
    reajuste = salario_novo - A


else:
    salario_novo = A * 1.04 
    percentual_ganho = 4
    reajuste = salario_novo - A
    
print(f"Novo salario: {salario_novo:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual_ganho} %")