class Calculadora:
    # Método que simula sobrecarga usando *args e **kwargs
    def soma(self, *args, **kwargs):
        # Se nenhum argumento foi passado
        if len(args) == 0 and len(kwargs) == 0:
            return "Nada a somar"

        # Somar os valores passados em args
        total_args = sum(args)

        # Somar os valores passados em kwargs
        total_kwargs = sum(kwargs.values())

        return total_args + total_kwargs

# Exemplo de uso
calc = Calculadora()

# Somar dois valores usando *args
print(calc.soma(58, 10))  # Saída: 15

# Somar múltiplos valores usando *args
print(calc.soma(6, 1, 2, 1))  # Saída: 10

# Somar usando **kwargs
print(calc.soma(a=25, b=50))  # Saída: 5

# Combinação de *args e **kwargs
print(calc.soma(10, 20, x=5, y=15))  # Saída: 50

# Nenhum argumento passado
print(calc.soma())  # Saída: Nada a somar

