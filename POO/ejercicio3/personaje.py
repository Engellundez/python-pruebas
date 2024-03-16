class Personaje():
    def __init__(self,nombre,fuerza,velocidad) -> None:
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self) -> str:
        return f'{self.nombre} (Fuerza: {self.fuerza}, Velociad: {self.velocidad})'
    
    def __add__(self, otro):
        nuevo_nombre = f'{self.nombre}-{otro.nombre}'
        nueva_fuerza = round(((self.fuerza + otro.fuerza) / 2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro.velocidad) / 2)**1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    