from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
from Biblioteca import Biblioteca
from Livro import Livro
from Autor import Autor
import datetime
import time



def main():

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    bot.browse("C:\\Users\\dsg02\\OneDrive\\Documentos\\GitHub\\Aulas-HyperAutomation\\POO\\Livro\\Composicao_Livro\\emprestimo.html")

    autor_acotar = Autor("Sarah J. Maas")
    # Adicionando os livros da série ACOTAR
    livro1 = Livro("A Court of Thorns and Roses", autor_acotar, "ACOTAR01")
    livro2 = Livro("A Court of Mist and Fury", autor_acotar, "ACOTAR02")
    livro3 = Livro("A Court of Wings and Ruin", autor_acotar, "ACOTAR03")
    livro4 = Livro("A Court of Frost and Starlight", autor_acotar, "ACOTAR04")
    livro5 = Livro("A Court of Silver Flames", autor_acotar, "ACOTAR05")

    biblioteca = Biblioteca("Biblioteca Central")
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)
    biblioteca.adicionar_livro(livro4)
    biblioteca.adicionar_livro(livro5)

    cliente_nome = "Daniele"
    livro_para_emprestimo = "ACOTAR01"  
    
    print("Preenchendo o formulário...") 
    bot.find_element("cod_livro", By.ID).send_keys(livro_para_emprestimo)
    time.sleep(1)
    bot.find_element("nome_cliente", By.ID).send_keys(cliente_nome)
    time.sleep(1)
    bot.find_element("livro_id", By.ID).send_keys(livro_para_emprestimo)
    time.sleep(1)
    bot.find_element("usuario_id", By.ID).send_keys("123") 
    time.sleep(1)

    data_emprestimo = datetime.date.today().strftime("%Y-%m-%d")
    data_devolucao = (datetime.date.today() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    
    bot.find_element("data_emprestimo", By.ID).send_keys(data_emprestimo)
    time.sleep(1)
    bot.find_element("data_devolucao", By.ID).send_keys(data_devolucao)
    time.sleep(1)

    print("Salvando os dados no arquivo...") 
    try:
        with open("emprestimo_dados.txt", "a", encoding="utf-8") as file:
            file.write(f"\nEmpréstimo registrado em {datetime.datetime.now()}\n")
            file.write(f"Código do Livro: {livro_para_emprestimo}\n")
            file.write(f"Nome do Cliente: {cliente_nome}\n")
            file.write(f"ID do Livro: {livro_para_emprestimo}\n")
            file.write(f"ID do Usuário: 123\n")
            file.write(f"Data de Empréstimo: {data_emprestimo}\n")
            file.write(f"Data de Devolução: {data_devolucao}\n")
            file.write(f"{'-'*40}\n") 
        print("Dados salvos com sucesso.") 
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}") 

    bot.wait(3000)
    bot.stop_browser()

if __name__ == '__main__':
    main()
