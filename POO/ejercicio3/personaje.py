class Personaje():
    def __init__(self,nombre,fuerza,velocidad) -> None:
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self) -> str:
        return f'{self.nombre} (Fuerza: {self.fuerza}, Velociad: {self.velocidad})'
    
    def __add__(self, otro_pj):
        
        nuevo_nombre = f'{self.nombre}-{otro_pj.nombre}'
        # nueva_fuerza = self.fuerza + otro_pj.fuerza
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2)**1.34)
        # nueva_velocidad = self.velocidad + otro_pj.velocidad
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad) / 2)**1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
    
# goku = Personaje("Goku", 100,100)
# vegeta = Personaje("Vegeta", 99,99)
# jiren = Personaje("Jiren", 130,140)

# print(goku, vegeta)
# gogeta = goku + vegeta
# jireta = gogeta + jiren

# print(jireta)
# print(gogeta)
# print(goku)
# print(vegeta)
# print(jiren)

while True:
    print(""" COMO SERIAN LA FUCIONES DE TUS PERSONAJES FAVORITOS \n
          OPCIONES: \n
          1: Crear Personaje \n
          2: Fusionar personajes \n
          3: Mostrar personajes \n
          4: Salir \n
          """)
    
    try:
        opcion = int(input("Selecciona una opción: "))
    except:
        print("Ocupo que escribas un numero, si no no puedo avanazar 😢😢 ")
    
    if opcion == 1:
        print("crea")
    elif opcion == 2:
        print("fusion")
    elif opcion == 3:
        print("muestra personajes")
    elif opcion == 4:
        break
    else:
        print('Pasame una opción valida')