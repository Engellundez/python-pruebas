# Al trabajar con Objetos se utiliza PascalCase TodasLasInicialesEnMayúsculas
class Celular:
    def __init__(self, marca, modelo, camera):
        self.marca = marca
        self.modelo = modelo
        self.camera = camera
        
    def llamar(self, numero):
        print(f"Estas llamando desde un {self.marca} al numero: {numero}")
        
    def colgar(self):
        print(f"Colgaste desde tu {self.modelo}")
    

Celular1 = Celular("Samsumng", "S23","48MP")
Celular2 = Celular("Apple", "Iphone 15 Pro","96MP")

# Objeto == instancia de la clase.

Celular1.llamar("4433867825")
Celular2.llamar("4433867825")
Celular2.colgar()
