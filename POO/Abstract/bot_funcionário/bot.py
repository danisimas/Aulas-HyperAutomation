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
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False
import json


json_data = '''
[
  {
    "nome": "João Silva",
    "matricula": "001",
    "numeroProjetos": 3,
    "tipoFuncionario": "Mensalista",
    "salarioBase": 3000.00,
    "comissao": 0,
    "totalVendas": 0,
    "valorHora": 0,
    "horasPorDia": 0
  },
  {
    "nome": "Maria Oliveira",
    "matricula": "002",
    "numeroProjetos": 5,
    "tipoFuncionario": "Comissionado",
    "salarioBase": 1500.00,
    "comissao": 5,
    "totalVendas": 20000.00,
    "valorHora": 0,
    "horasPorDia": 0
  },
  {
    "nome": "Carlos Souza",
    "matricula": "003",
    "numeroProjetos": 2,
    "tipoFuncionario": "Horista",
    "salarioBase": 0,
    "comissao": 0,
    "totalVendas": 0,
    "valorHora": 20.00,
    "horasPorDia": 8
  }
]
'''

def ler_funcionarios(json_data):
    try:
        # Carrega o JSON e transforma em uma lista de dicionários
        funcionarios = json.loads(json_data)
        return funcionarios
    except json.JSONDecodeError as e:
        print(f"Erro ao ler o JSON: {e}")
        return []


def preencher_campo(bot, lista):

    


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    bot.execute(r"C:\Users\dsg02\OneDrive\Documentos\GitHub\Aulas-HyperAutomation\POO\Abstract\tkinter\dist\dani.exe")
    

     
     
     
    
    
    
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