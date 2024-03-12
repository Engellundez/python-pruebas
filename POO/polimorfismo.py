class Animal():
    def sonido(self):
        pass

# class Gato():  #sin plimorfismo heredado
class Gato(Animal): # 
    def sonido(self):
        return "Miau"

# class Perro():  #sin plimorfismo heredado
class Perro(Animal): # 
    def sonido(self):
        return "Guau"


gato = Gato()
perro = Perro()

# print(gato.sonido())
# print(perro.sonido())

def hacer_sonido(animal):
    print(animal.sonido())

# hacer_sonido(gato)
# hacer_sonido(perro)



# ---------------------------------------------------------------------------------------------------------------------------------------
num1 = 3
num2 = 4.4

resultado = num1 + num2

print(resultado)
print(type(resultado))