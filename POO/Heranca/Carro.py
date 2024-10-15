class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    
    def informacao(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas
    
    def informacao(self):
        return f"{super().informacao()}, Número de portas: {self.num_portas}"

if __name__ == '__main__':
    carro = Carro("Fiat", "Uno", 4)
    print(carro.informacao())
    veiculo = Veiculo("Ford", "Mustang")
    veiculo1 = Veiculo("Honda", "Honda Hrv")
    carro1  = Carro(veiculo.marca, veiculo.modelo, 4)
    carro2 = Carro(veiculo1.marca, veiculo1.modelo, 6)
    print(carro1.informacao())
    print(carro2.informacao())

