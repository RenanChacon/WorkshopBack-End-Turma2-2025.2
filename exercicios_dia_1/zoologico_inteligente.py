class Zoologico():
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def listar_animais(self):
        print('Lista de Animais:')
        for animal in self.animais:
            print(f"Animal: {animal.nome} / Idade: {animal.idade} / Som: {animal.falar()}")

    def listar_tipo(self, tipo):
        print(f'Lista de {tipo}s:')

        for animal in self.animais:
            if isinstance(animal, tipo):
                print(f"Animal: {animal.nome} / Idade: {animal.idade} / Som: {animal.falar()}")

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
c = Cachorro('Luck', 5)
z = Zoologico()

z.adicionar_animal(g)
z.adicionar_animal(c)
z.listar_animais()
z.listar_tipo(Gato)



