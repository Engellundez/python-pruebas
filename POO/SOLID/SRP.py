# Principio de propósito Único

# El tanque se lleva por separado
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        if (cantidad > 0 and cantidad <= 100):
            self.combustible += cantidad
        elif(cantidad > 100):
            espacio_disponible = 100 - self.cantidad_combustible
            print(f'canti {self.cantidad_combustible}')
            print(f'diponible {espacio_disponible}')
            combustible_desperdiciado = cantidad - espacio_disponible
            self.combustible = 100
            print(f"no hermano, al taque no le cabe más has tirado {combustible_desperdiciado}")
        else:
            print("que es eso hermano, esta pobre")
    
    @property
    def cantidad_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class NotTanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        if (cantidad > 0 and cantidad <= 100):
            self.combustible += cantidad
        elif(cantidad > 100):
            espacio_disponible = 100 - self.cantidad_combustible
            print(f'canti {self.cantidad_combustible}')
            print(f'diponible {espacio_disponible}')
            combustible_desperdiciado = cantidad - espacio_disponible
            self.combustible = 100
            print(f"no hermano, al taque no le cabe más has tirado {combustible_desperdiciado}")
        else:
            print("que es eso hermano, esta pobre")
    
    @property
    def cantidad_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

# auto espera una propiedad de TanqueDeCombustible, pero ambas funcionan por separado
class Auto:
    # : Class dice que mi variable depende del objeto de TanqueDeCombustible
    def __init__(self,tanque: TanqueDeCombustible):
        self.posición = 0
        self.tanque = tanque
    
    def mover(self, distancia):
        if self.tanque.cantidad_combustible >= distancia / 2:
            self.posición += distancia
            self.tanque.usar_combustible(distancia / 2)
        else: 
            print("No hay suficiente combustible")
            
    @property
    def posición_actual(self):
        return self.posición


tanque = TanqueDeCombustible()
not_tanque = NotTanqueDeCombustible()
vocho = Auto(tanque)
print(not_tanque.cantidad_combustible)
vocho2 = Auto(not_tanque)

vocho.mover(10)
vocho.mover(20)
vocho.mover(60)
vocho.mover(100)
vocho.mover(10)
print(vocho.posición_actual)
vocho.tanque.agregar_combustible(500)
print(vocho.posición_actual)
vocho.mover(200)
print(vocho.posición_actual, tanque.cantidad_combustible)
print(vocho2.posición_actual, not_tanque.cantidad_combustible)