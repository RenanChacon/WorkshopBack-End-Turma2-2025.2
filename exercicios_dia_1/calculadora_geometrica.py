import math

class FiguraGeometrica:
        
        @staticmethod
        def area_circulo(raio):
            return math.pi * math.pow(raio,2)

        @staticmethod
        def area_triangulo(base, altura):
            return base * altura / 2

        @staticmethod
        def hipotenusa_triangulo_retangulo(cateto1, cateto2):
            return math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))

def escolhe_calculo():
    escolha = input('Escolha o cálculo que deseja fazer(1-Area do circulo / 2-Area do triângulo / 3-Hipotenusa trângulo retângulo): ')

    if escolha == '1':
        raio = float(input('Digite o raio do círculo: '))
        return FiguraGeometrica().area_circulo(raio)
    
    elif escolha == '2':
        base = float(input('Digite o valor da base do triângulo: '))
        altura = float(input('Digite o valor da altura do triângulo: '))
        return FiguraGeometrica().area_triangulo(base, altura)
    
    elif escolha == '3':
        cateto1 = float(input('Digite o valor do cateto: '))
        cateto2 = float(input('Digite o valor do outro cateto: '))

        return FiguraGeometrica().hipotenusa_triangulo_retangulo(cateto1, cateto2)

    return 'opção inválida'

print(escolhe_calculo())