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
To fix this, you can either:if not bot.find( "campo_projetos", matching=0.97, waiting_time=10000):
    not_found("campo_projetos")
bot.click()

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
    "salarioBase": 3000,
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

funcionarios = json.loads(json_data)

def preencher_campos(bot):
    for func in funcionarios:
      if not bot.find( "campo_nome_func", matching=0.97, waiting_time=10000):
          not_found("campo_nome_func")
      bot.click()
      # 'kb_type' method receives text to be typed.
      bot.kb_type(str(func['nome']))
      
      if not bot.find( "campo_matricula_func", matching=0.97, waiting_time=10000):
          not_found("campo_matricula_func")
      bot.click()

      bot.kb_type(str(func['matricula']))
      
      if not bot.find( "campo_projetos", matching=0.97, waiting_time=10000):
          not_found("campo_projetos")
      bot.click()
      bot.kb_type(str(func['numeroProjetos']))
      
      tipo = str(func['tipoFuncionario'])
      
      if tipo == "Mensalista":
        
          
          if not bot.find( "campo_mensalista", matching=0.97, waiting_time=10000):
              not_found("campo_mensalista")
          bot.click()
          
         
          if not bot.find( "salario_base", matching=0.97, waiting_time=10000):
              not_found("salario_base")
          bot.click()
          bot.kb_type(str(func['salarioBase']))

          if not bot.find( "botão_cad_func_mensal", matching=0.97, waiting_time=10000):
              not_found("botão_cad_func_mensal")
          bot.click()
          if not bot.find( "fechar_campo_botão", matching=0.97, waiting_time=10000):
              not_found("fechar_campo_botão")
          bot.click()
      
      elif tipo == "Horalista":
          
          if not bot.find( "campo_horalista", matching=0.97, waiting_time=10000):
              not_found("campo_horalista")
          bot.click()

          if not bot.find( "campo_valor_hora", matching=0.97, waiting_time=10000):
              not_found("campo_valor_hora")
          bot.click()
          bot.kb_type(str(func['valorHora']))
          if not bot.find( "campo_horas_dia", matching=0.97, waiting_time=10000):
              not_found("campo_horas_dia")
          bot.click()
          bot.kb_type(str(func['horasPorDia']))
          
          if not bot.find( "botão_cad_func_mensal", matching=0.97, waiting_time=10000):
             not_found("botão_cad_func_mensal")
          bot.click()
          if not bot.find( "fechar_campo_botão", matching=0.97, waiting_time=10000):
             not_found("fechar_campo_botão")
          bot.click()
      else:
         
          if not bot.find( "comissario", matching=0.97, waiting_time=10000):
              not_found("comissario")
              bot.click()
         
          if not bot.find( "salario_base", matching=0.97, waiting_time=10000):
              not_found("salario_base")
          bot.click()
          bot.kb_type(str(func['salarioBase']))
          
          if not bot.find( "campo_comissao", matching=0.97, waiting_time=10000):
              not_found("campo_comissao")
          bot.click()
          bot.kb_type(str(func['comissao']))
          
          if not bot.find( "campo_total_vendas", matching=0.97, waiting_time=10000):
              not_found("campo_total_vendas")
          bot.click()
          bot.kb_type(str(func['total_vendas']))

          if not bot.find( "botão_cad_func_mensal", matching=0.97, waiting_time=10000):
              not_found("botão_cad_func_mensal")
          bot.click()
          if not bot.find( "fechar_campo_botão", matching=0.97, waiting_time=10000):
              not_found("fechar_campo_botão")
          bot.click()
        
          
       
     
        



def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    bot.execute(r"C:\\Users\\matutino\\Downloads\\Daniele Simas\\Aulas-HyperAutomation\\POO\\Abstract\\tkinter\\dist\\dani.exe")
    
    preencher_campos(bot)

     
     
     
    
    
    
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



