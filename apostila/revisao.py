# Team Phoenix: Marielle, Daniele, Carlos e Luiz

compras = []

while True:
    print("""\nMenu:
1. Adicionar itens
2. Remover itens
3. Exibir itens
4. Buscar itens
5. Sair\n
""")
    operacao = int(input("Escolha uma opção: "))

    match(operacao):
        case 1:
            num = input("Digite o nome do item: ")
            compras.append(num)
            print("Item adicionado com sucesso")
        case 2:
            if (len(compras)==0):
                print("Impossível remover itens\n")
            else:
                rmv = input("Digite o nome do item para remover: ")
                if rmv in compras:
                    compras.remove(rmv)
                    print("Item removido")
                else:
                    print("Item não está na lista")
        case 3:
            for i in compras:
                print(i)
        case 4:
            rmv = input("Digite o nome do item para pesquisar: ")
            if (rmv in compras):
                print("Item pesquisado: ",rmv)
            else:
                print("Item não encontrado")    

        case 5:
            break