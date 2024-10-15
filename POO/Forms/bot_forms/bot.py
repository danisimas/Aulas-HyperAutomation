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

from Forms.FormLogin import FormLogin

from webdriver_manager.chrome import ChromeDriverManager 
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


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
    bot.driver_path = ChromeDriverManager().install()

    # Opens the BotCity website.
    bot.browse("file:///C:/Users/matutino/Downloads/Daniele%20Simas/Aulas-HyperAutomation/POO/Forms/forms_teste.html")

    forms_dados = FormLogin('Daniele Simas', "daniele@example.com", "StrongPassword@1!", "12345678901")

    bot.wait(5000)

    bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(forms_dados.nome)

    bot.wait(5000)

    bot.find_element('//*[@id="email"]', By.XPATH).send_keys(forms_dados.email)
    
    bot.find_element('//*[@id="password"]', By.XPATH).send_keys(forms_dados.password)

    bot.wait(5000)

    bot.find_element('//*[@id="nomeForm"]/form/button', By.XPATH).click()



    bot.wait(5000)

    bot.find_element('/html/body/div/div[1]/div[2]', By.XPATH).click()
    bot.find_element('//*[@id="telefone"]', By.XPATH).send_keys(forms_dados.telefone)

    bot.wait(5000)

    bot.find_element('//*[@id="contatoForm"]/form/button', By.XPATH).click()

    bot.wait(5000)

    bot.find_element('/html/body/div/div[1]/div[3]', By.XPATH).click()

    bot.find_element('//*[@id="emailLogin"]', By.XPATH).send_keys(forms_dados.email)

    bot.find_element('//*[@id="passwordLogin"]', By.XPATH).send_keys(forms_dados.password)

    bot.find_element('//*[@id="loginForm"]/form/button', By.XPATH).click()
    bot.wait(5000)

    bot.stop_browser()





    # Wait 3 seconds before closing
    #bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    

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
