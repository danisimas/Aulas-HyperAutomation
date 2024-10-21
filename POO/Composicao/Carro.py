class Motor():
    def ligar(self):
        print("Motor ligado")

class Carro():
    def __init__(self, modelo):
        self.motor = Motor()
        self.modelo = modelo
    
    def ligar(self):
        self.motor.ligar()
        print(f"Carro {self.modelo} ligado")



if __name__ == "__main__":
    carro = Carro("Ferrari")
    carro.ligar()

