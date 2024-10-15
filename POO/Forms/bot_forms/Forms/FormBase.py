import re

class FormBase:
    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = password
    
    def validar_email(self):
        if '@' in self.email and '.' in self.email:
            return True
        else:
            return False
    
    def validar_senha(self):
       
        if len(self.password) < 8:
            return False

        if (re.search(r"[A-Z]", self.password) and     
            re.search(r"[a-z]", self.password) and    
            re.search(r"[0-9]", self.password) and     
            re.search(r"[@#$%^&+=!]", self.password)): 
            return True
        else:
            return False