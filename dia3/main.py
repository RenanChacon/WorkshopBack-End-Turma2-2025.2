'''
Exercício 1

print("Olá, mundo!"
Falta fechar o parêntese

Correção:
'''

print("Olá, mundo!") 

'''
Exercício 2

print(nome)
Falta declarar a variável

Correção:
'''
nome = 'Renan'
print(nome) 

'''
Exercíco 3 

def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado)

Está tentando somar um int com uma string

Correção:
'''
def somar(a, b):
    return int(a) + int(b) 

resultado = somar(10, "5")
print(resultado) 

'''
Exercício 4

numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])

O programa quebra caso o índice digitao não existir na lista

Correção:
'''
numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

try:
    print(numeros[indice])
except IndexError:
    print("O índice digitado não exite na lista.") 

'''
Exercício 5

def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")

O código quebra caso os valores digitados não sejam numeros ou sejam 
numeros com casas decimais ou o segundo valor seja 0

Correção:
'''

def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

try:
    resultado = dividir(int(num1), int(num2))
except ValueError:
    print("Valor digitado inválido, por favor digite apenas números inteiros.")
except ZeroDivisionError:
    print("Dividir qualquer número por zero é impossível.")

print(f"Resultado: {resultado}")

'''
Exercício 6

dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

print(f"O valor da chave '{chave}' é: {dados[chave]}")

O códico quebra caso seja digitado uma chave que não existe no dicionário


Correção:
'''
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}

chave = input("Digite a chave que deseja acessar: ")

print(f"O valor da chave '{chave}' é: {dados.get(chave, "Erro, essa chave não existe.")}")

'''
Exercício 7
'''