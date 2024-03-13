import os 
class Personaje():
    def __init__(self,nombre,fuerza,velocidad) -> None:
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self) -> str:
        return f'{self.nombre} (Fuerza: {self.fuerza}, Velociad: {self.velocidad})'
    
    def __add__(self, otro_pj):
        nuevo_nombre = f'{self.nombre}-{otro_pj.nombre}'
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza) / 2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.velocidad) / 2)**1.34)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
def clear():
    os.system("clear")
    
def mostrar_personajes():
    print('Estos son los personajes que se han creado.\n')
    
    if(personajes.__len__() == 0):
        print('No se han encontrado personajes 😢😢\n\n')
    else:
        for index, personaje in enumerate(personajes):
            print(f'{index+1}.- {personaje}')
        print('\n\n')

def solicitud_segura_int(mensaje_input,mensaje_error="ese dato no lo puedo procesar asi que..."):
    while True:
        try:
            dato = int(input(mensaje_input))
            break
        except ValueError:
            print(mensaje_error)
    
    return dato

def crear_personaje(nombre,fuerza,velocidad):
    nuevo_personaje = Personaje(nombre,fuerza,velocidad)
    personajes.append(nuevo_personaje)
    clear()
    print("Personaje creado adecuadamente.")
    print(nuevo_personaje,'\n\n')

def solicitar_personaje(mensaje_input="Escoge un personaje: "):
    while True:
        mostrar_personajes()
        elegido = solicitud_segura_int(mensaje_input) - 1
        clear()
        try:
            personaje = personajes[elegido]
            del elegido
            break
        except:
            print("No encuentro a los personajes que buscas, hay que tratar de nuevo\n\n")
    return personaje
                
personajes = []

while True:
    clear()
    opt = 0
    opt = solicitud_segura_int("""COMO SERIAN LA FUSIONES DE TUS PERSONAJES FAVORITOS \n
                OPCIONES
          1: Crear Personaje
          2: Fusionar personajes
          3: Mostrar personajes
          4: Editar personaje
          5: Salir
          
Selecciona una opción: """, "Ocupo que escribas un numero, si no no puedo avanazar 😢😢 ")
    clear()
    
    if opt == 1:
        nombre = input("Momento de crear un nuevo personaje\n\n Como se llamara: ")
        fuerza = solicitud_segura_int("¿Cual sera su fuerza?: ")
        velocidad = solicitud_segura_int("¿y su velocidad?: ")
        
        crear_personaje(nombre,fuerza,velocidad)    
    elif opt == 2:
        if(personajes.__len__() < 2):
            print("Woooops ay un fallo en la matrix, no hay suficientes personajes para hacer la fusión :(\n\n")
            continue

        personaje1 = solicitar_personaje("Escoge al primer personaje: ")
        personaje2 = solicitar_personaje("Escoge al segundo personaje: ")
        
        nueva_fusion = personaje1 + personaje2
        personajes.append(nueva_fusion)
        clear()
        print("Personaje fusionado adecuadamente")
        print(nueva_fusion,'\n')
    elif opt == 3:
        mostrar_personajes()
    elif opt == 4:
        if(personajes.__len__() < 1):
            print("Woooops ay un fallo en la matrix, no hay personajes para editar :(\n\n")
            continue
        
        personaje_editar = solicitar_personaje('¿Cual personaje vamos a editar?✍🏼✍🏼✍🏼✍🏼: ')
        while True:
            print(f'Que datos le vamos a editar a: {personaje_editar}')
            editar_opt = solicitud_segura_int("\n1.-Nombre\n2.-Fuerza\n3.-Velocidad\n4-....- Salir\n\nEscoge una opción:")
            
            clear()
            print(personaje_editar,'\n')
            match editar_opt:
                case 1:
                    personaje_editar.nombre = input("¿Cual es el nuevo nombre de tu personaje? ")
                case 2:
                    personaje_editar.fuerza = solicitud_segura_int("¿Cual es la nueva fuerza de tu personaje? ")
                case 3:
                    personaje_editar.velocidad = solicitud_segura_int("¿Cual es la nueva velocidad de tu personaje? ")
                case _:
                    break
        
            clear()
            print(f'El personaje se ha editado correctamente \n\n       {personaje_editar}\n')           
    elif opt == 5:
        print("Bye Bye")
        break