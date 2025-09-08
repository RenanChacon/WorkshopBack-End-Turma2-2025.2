class Animal:
    def falar(self):
        ...

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

g = Gato()
c = Cachorro()

print(g.falar())
print(c.falar())


