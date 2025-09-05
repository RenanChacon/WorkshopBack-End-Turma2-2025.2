import math

def pede_numero():
    return float(input('Digite um número: '))

def arredonda_baixo():
    return math.floor(pede_numero())

def arredonda_cima():
    return math.ceil(pede_numero())

def arredonda_inteiro():
    return round(pede_numero())

print(arredonda_baixo())
print(arredonda_cima())
print(arredonda_inteiro())
