"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

from webdriver_manager.chrome import ChromeDriverManager


# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


class Produtos:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
    
    def atualizar_produto(self, produto):
        self.nome = produto.nome
        self.preco = produto.preco
        self.quantidade = produto.quantidade
    
    


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    bot.driver_path = ChromeDriverManager().install()

    # Opens the BotCity website.
    bot.browse("http://127.0.0.1:5000/")

    produto = Produtos("Telefone", 50, 100)

    bot.find_element('//*[@id="nome"]',By.XPATH).send_keys(produto.nome)
    bot.find_element('//*[@id="preco"]', By.XPATH).send_keys(produto.preco)
    bot.find_element('//*[@id="quantidade"]', By.XPATH).send_keys(produto.quantidade)
    bot.find_element('/html/body/div/form/input[4]', By.XPATH).click()

    # Wait 3 seconds before closing
    bot.wait(6000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
