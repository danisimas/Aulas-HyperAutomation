
from Excecoes import ValorInvalidoError
from Excecoes import QuantidadeInvalidaError
from Produto import Produto
from Pedido import Pedido
from GestorDePedidos import GestorDePedidos



# Testes para as classes



# Teste de criação de um produto válido
try:
    produto1 = Produto("Celular", 1500, "Eletrônicos")
    print(produto1.detalhes())
except ValorInvalidoError as e:
    print(f"Erro ao criar produto: {e}")

# Teste de criação de um produto com preço inválido
try:
    produto_invalido = Produto("Tablet", -500, "Eletrônicos")
except ValorInvalidoError as e:
    print(f"Erro ao criar produto: {e}")

# Teste de criação de um pedido válido
produto2 = Produto("Notebook", 3000, "Eletrônicos")
produto3 = Produto("Mouse", 50, "Acessórios")
try:
    pedido1 = Pedido([produto2, produto3], {produto2: 1, produto3: 2}, "Cliente A")
    print(pedido1.detalhes_pedido())
except QuantidadeInvalidaError as e:
    print(f"Erro ao criar pedido: {e}")

# Teste de criação de um pedido com quantidade inválida
try:
    pedido_invalido = Pedido([produto2], {produto2: -1}, "Cliente B")
except QuantidadeInvalidaError as e:
    print(f"Erro ao criar pedido: {e}")

# Teste do método total_pedido
try:
    total = pedido1.total_pedido()
    print(f"Total do pedido: {total}")
except Exception as e:
    print(f"Erro ao calcular o total do pedido: {e}")

# Criando o gestor de pedidos
gestor = GestorDePedidos()

# Adicionando um pedido válido
try:
    gestor.adicionar_pedido(pedido1)
    print("Pedido adicionado com sucesso!")
except Exception as e:
    print(f"Erro ao adicionar pedido: {e}")

# Listando pedidos com status "Novo"
try:
    pedidos_novos = gestor.listar_pedidos_por_status("Novo")
    for pedido in pedidos_novos:
        print(pedido.detalhes_pedido())
except Exception as e:
    print(f"Erro ao listar pedidos por status: {e}")

# Salvando e carregando dados em JSON
try:
    gestor.salvar_dados_json("pedidos.json")
    print("Dados salvos em JSON com sucesso.")
    gestor.carregar_dados_json("pedidos.json")
    print("Dados carregados de JSON com sucesso.")
except Exception as e:
    print(f"Erro ao manipular dados JSON: {e}")

# Salvando e carregando dados em binário
try:
    gestor.salvar_dados_binario("pedidos.pkl")
    print("Dados salvos em binário com sucesso.")
    gestor.carregar_dados_binario("pedidos.pkl")
    print("Dados carregados do binário com sucesso.")
except Exception as e:
    print(f"Erro ao manipular dados binários: {e}")

# Teste para verificar o log ao adicionar um pedido
gestor.adicionar_pedido(pedido1)

# Teste para verificar o log ao listar pedidos por status
gestor.listar_pedidos_por_status("Novo")