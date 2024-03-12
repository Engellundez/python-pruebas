class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        return f'Hola soy {self.nombre} y tengo {self.edad} años'
    
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
        
    def presentarse_con_grado(self):
        return f'{super().presentarse()}, y actualmente curso el {self.grado} grado.'

yo = Estudiante('Angel', 25, 9)

print(yo.presentarse_con_grado())