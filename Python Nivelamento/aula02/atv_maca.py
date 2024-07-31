# Exercicio 4


quant_maca = int(input("Digite a quantidade de maças compradas \n"))

if quant_maca <= 12:
    total = quant_maca * 0.25
    print(f"Total: {total}")
else:
    total = quant_maca * 0.30
    print(f"Total: {total}")