# Revisar esses pontos

dicionario = {}


while True:
    print("""\nMenu:
1. Adicionar animal
2. Exibir animais
3. Buscar animais
4. Sair\n
""")
    operacao = int(input("Escolha uma opção: "))

    match(operacao):
        case 1:
            animal_novo = input("Nome do animal e sua descrição: ").split()
            dicionario[animal_novo[0]] = animal_novo[1]           
            print("Animal adicionado com sucesso")
        case 2:
            print(dicionario)
        case 3:
            nome = input("Nome do animal que deseja pesquisar: ")
            print("Descrição:",  dicionario[nome])

        case 4:
            break

