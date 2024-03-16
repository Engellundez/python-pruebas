import os 
from personaje import Personaje

def clear():
    # para que siempre funcione
    os.system('cls' if os.name == 'nt' else 'clear')
    
def mostrar_personajes(personajes):
    print('Estos son los personajes que se han creado:\n')
    
    if not personajes:
        print('No se han encontrado personajes 😢😢\n\n')
    else:
        for index, personaje in enumerate(personajes):
            print(f'{index+1}.- {personaje}')
        print('\n')

def solicitud_segura_int(mensaje_input,mensaje_error="Ese dato no lo puedo procesar, intenta de nuevo con un número: "):
    while True:
        try:
            return int(input(mensaje_input))
        except ValueError:
            print(mensaje_error)

def crear_personaje():
    nombre = input("Momento de crear un nuevo personaje\n\n Como se llamara: ")
    fuerza = solicitud_segura_int("¿Cual sera su fuerza?: ")
    velocidad = solicitud_segura_int("¿y su velocidad?: ")
        
    return Personaje(nombre,fuerza,velocidad)

def solicitar_personaje(personajes, mensaje_input="Escoge un personaje: "):
    while True:
        mostrar_personajes(personajes)
        try:
            indice = solicitud_segura_int(mensaje_input) - 1
            return personajes[indice]
        except:
            clear()
            print("No encuentro a los personajes que buscas, hay que tratar de nuevo\n\n")

def editar_personaje(personaje):
    while True:
        print(f'Que datos le vamos a editar a: {personaje}')
        opt = solicitud_segura_int("\n1.-Nombre\n2.-Fuerza\n3.-Velocidad\n4-Salir\n\nEscoge una opción: ")
        clear()
        
        if opt == 1:
            personaje.nombre = input("¿Cual es el nuevo nombre de tu personaje? ")
        elif opt == 2:
            personaje.fuerza = solicitud_segura_int("¿Cual es la nueva fuerza de tu personaje? ")
        elif opt == 3:
            personaje.velocidad = solicitud_segura_int("¿Cual es la nueva velocidad de tu personaje? ")
        elif opt == 4:
            break
            
        clear()
        print(f'El personaje se ha editado correctamente \n\n       {personaje}\n') 

def main():
    personajes = []

    while True:
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
            personaje = crear_personaje()
            personajes.append(personaje)
            print("Personaje creado correctamente: ", personaje, '\n')
        elif opt == 2:
            if(len(personajes) < 2):
                print("Woooops ay un fallo en la matrix, no hay suficientes personajes para hacer la fusión :(\n")
                continue

            personaje1 = solicitar_personaje(personajes,"Escoge al primer personaje: ")
            personaje2 = solicitar_personaje(personajes,"Escoge al segundo personaje: ")

            nuevo_personaje = personaje1 + personaje2
            personajes.append(nuevo_personaje)
            print("Personaje fusionado adecuadamente")
        elif opt == 3:
            mostrar_personajes(personajes)
        elif opt == 4:
            if not personajes:
                print("Woooops ay un fallo en la matrix, no hay personajes para editar :(\n\n")
                continue
            
            personaje_editar = solicitar_personaje(personajes,'¿Cual personaje vamos a editar?✍🏼✍🏼✍🏼✍🏼: ')
            editar_personaje(personaje_editar)          
        elif opt == 5:
            print("Bye Bye")
            break

main()