from abc import ABC, abstractclassmethod

# class Trabajador(ABC):
#     # INTERFAZ
#     @abstractclassmethod
#     def comer(self):
#         pass
#     # QUE NO JALA PORQUE NO TODO
#     @abstractclassmethod
#     def trabajar(self):
#         pass
#     # LO HACE UN TRABAJADOR.
#     @abstractclassmethod
#     def dormir(self):
#         pass

# FORMA CORRECTA DE HACERLO
class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass
    
class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass
    
class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass


class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("El humano está comiendo")
        
    def trabajar(self):
        print("El humano está trabajando")
        
    def dormir(self):
        print("El humano está durmiendo")


# class Robot(Trabajador):
#     def comer(self):
#         # aquí se llama una interfaz que no se usa, aquí no jala el principio
#         pass
        
#     def trabajar(self):
#         print("El humano está trabajando")
        
#     def dormir(self):
#         # aquí se llama una interfaz que no se usa, aquí no jala el principio
#         pass
    

class Robot(Trabajador):        
    def trabajar(self):
        print("El robot está trabajando")
    
robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()
humano.comer()
humano.dormir()