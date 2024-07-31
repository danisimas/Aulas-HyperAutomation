vendas = []

def listar_vendas(lista_vendas):
    for venda in lista_vendas:
        print(venda)

def inserir_vendas(lista_vendas):
    venda = float(input("Digite o valor da venda: "))
    lista_vendas.append(venda)


def total_vendas(lista_vendas):
    return sum(lista_vendas)


def media_vendas(lista_vendas):
    return sum(lista_vendas) / len(lista_vendas)


def maior_venda(lista_vendas):
    return max(lista_vendas)


while True:
    print("""\nMenu:
1. Inserir vendas
2. Listar vendas
3. Exibir o total de vendas
4. Média das vendas
5. Exibir o maior valor das vendas
6. Sair\n
""")
    operacao = int(input("Escolha uma opção: "))

    match(operacao):
        case 1:
            inserir_vendas(vendas)
            print("Venda inserida com sucesso")  
        case 2:
           print("Listagem de vendas")
           listar_vendas(vendas) 
        case 3:
            print("Total de vendas")
            print(total_vendas(vendas))
        case 4:
            print("Média das vendas")
            print(media_vendas(vendas))
        case 5:
            print("Maior valor das vendas")
            print(maior_venda(vendas))
        case 6:
            break
