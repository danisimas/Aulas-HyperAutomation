from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
import time
from Veiculo import Veiculo, Carro, Moto  # Importando as classes definidas

def main():
    # Configura o bot para navegar até a página
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    # Abre a página HTML de gerenciamento de veículos
    bot.browse("C:\\Users\\dsg02\\OneDrive\\Documentos\\GitHub\\Aulas-HyperAutomation\\POO\\Heranca\\ex6\\site.html")

    # Criação de veículos usando as classes Carro e Moto
    veiculos = [
        Carro("Toyota Corolla", 2021, 150, "Gasolina"),
        Moto("Honda CB500", 2019, 80, 500)
    ]

    for veiculo in veiculos:
        print(f"Preenchendo formulário para: {veiculo.get_nome()}")

        # Preenche o campo Nome do Veículo
        bot.find_element("vehicleName", By.ID).send_keys(veiculo.get_nome())
        time.sleep(1)

        # Preenche o campo Ano
        bot.find_element("vehicleYear", By.ID).send_keys(str(veiculo.get_ano()))
        time.sleep(1)

        # Preenche o campo Valor Diário
        bot.find_element("rentalValue", By.ID).send_keys(str(veiculo.get_valor_diario()))
        time.sleep(1)

        # Preenche o campo de Tipo de Veículo e o campo extra (combustível ou cilindrada)
        if isinstance(veiculo, Carro):
            bot.find_element("vehicleType", By.ID).click()
            bot.find_element("//option[@value='carro']", By.XPATH).click()
            time.sleep(1)
            bot.find_element("extraFieldInput", By.ID).send_keys(veiculo.tipo_combustivel)
        elif isinstance(veiculo, Moto):
            bot.find_element("vehicleType", By.ID).click()
            bot.find_element("//option[@value='moto']", By.XPATH).click()
            time.sleep(1)
            bot.find_element("extraFieldInput", By.ID).send_keys(str(veiculo.cilindrada))

        # Preenche o campo Número de Dias
        days = 5
        bot.find_element("rentalDays", By.ID).send_keys(str(days))
        
        # Clica no botão "Calcular Aluguel"
        bot.find_element("//*[@id='vehicleForm']/div[2]/button[2]", By.XPATH).click()
        time.sleep(1)

        # Limpa os campos para o próximo veículo
        bot.find_element("vehicleName", By.ID).clear()
        bot.find_element("vehicleYear", By.ID).clear()
        bot.find_element("rentalValue", By.ID).clear()
        bot.find_element("extraFieldInput", By.ID).clear()
        bot.find_element("rentalDays", By.ID).clear()

        time.sleep(2)

    print("Automação completa.")

    bot.wait(5000)
    bot.stop_browser()

if __name__ == '__main__':
    main()
