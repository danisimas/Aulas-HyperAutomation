
salario = float(input())
if salario <= 2000.00:
     print("Isento")
elif salario <= 3000.00:
    imposto = (salario - 2000.00) * 0.08
    print(f"R$ {imposto:.2f}")
elif salario <= 4500.00:
    imposto = (salario - 3000.00) * 0.18 + 1000.00 * 0.08
    print(f"R$ {imposto:.2f}")
else:
    imposto = (salario - 4500.00) * 0.28 + 1500.00 * 0.18 + 1000.00 * 0.08
    print(f"R$ {imposto:.2f}")