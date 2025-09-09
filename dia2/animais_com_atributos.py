class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'Nome: {self.nome} \nIdade: {self.idade}'

    def falar(self):
        ...

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def apresentar(self):
        return super().apresentar()
    
    def falar(self):
        return "Miau!"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

g = Gato('Felix', 10)


print(g.apresentar())



