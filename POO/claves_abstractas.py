# abc = modulo de python, ABC = clase, abstractclassmethod = decorador
from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    # El hacer una funcion abstracta obligamos a la clase hija a generar una clase con el mismo nombre para funcionar
    # en caso de no existir el código va a dar error. 
    # y al usarlo fomentamos el polimorfismo de clases.
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print (f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")
        

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")
    
angel = Estudiante("Angel",25,"Masculino","Programación")
gio = Trabajador("Gio",25,"No binario","Programación")

def realizar_actividad(funcion):
    funcion.hacer_actividad()
        

angel.presentarse()
realizar_actividad(angel)
gio.presentarse()
realizar_actividad(gio)
