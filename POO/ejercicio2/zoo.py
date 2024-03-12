class Animal:
    def __init__(self,animal):
        self.animal = animal
    
    def comer(self):
        return f'El {self.animal} está comiendó'
    

class Mamifero(Animal):        
    def amamantar(self):
        return f'{super().comer()}, mientras es amamantado por su madre'
    
    
class Ave(Animal):    
    def volar(self):
        return f'El {self.animal} está volando woooooow'


class Murcielago(Mamifero, Ave):
        pass
        
        
murcielago = Murcielago("Murcielago")

print(murcielago.animal)
print(murcielago.volar())
print(murcielago.amamantar())

print(Murcielago.mro())