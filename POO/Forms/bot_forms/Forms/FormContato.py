
from Forms.FormBase import FormBase

class FormContato(FormBase):
    def __init__(self, nome, email, password, telefone):
        super().__init__(nome, email, password)
        self.telefone = telefone
    
    def validar_telefone(self):
        if len(self.telefone) == 11 and self.telefone.isdigit():
            return True
        else:
            return False



    