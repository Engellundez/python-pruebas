#falto el profe y los pibes se la saben asi que ellos dan la clase, el mayor la da y el menor lo asiste, pedir nombre y edad a cada alumno para el ejercicio.

def obtener_compañeros(cantidad):
    compañeros = []

    for i in range(cantidad):
        nombre = input(f'¿Como se llama el compañero {i+1}?: ')
        edad = int(input(f'¿Que edad tiene {nombre}?: '))

        compañero = (nombre,edad)
        compañeros.append(compañero)
    
    compañeros.sort(key=lambda x : x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return profesor,asistente

cantidad_alumnos = int(input('Hola, soy la directora, Ya que el profe no vino. ¿Cuantos vinieron a clases?: '))
profesor,asistente = obtener_compañeros(cantidad_alumnos)

print(f'El profesor sera {profesor} y su asistente sera {asistente}, pueden comenzar la clase...')