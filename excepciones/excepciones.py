# Creando función que suma numero son su excepciones contempladas
def sumar_dos():
    # Inicia el bucle
    while True:
        # Pidiendo números al usuario
        a = input("Numero 1: ")
        b = input("Numero 2: ")
    
        # intentando convertir los a entero y sumar los 
        try:
            resultado = int(a) + int(b)
        # si lanzo una excepción, pedirle que ingrese los datos
        except Exception as e:
            print("Te pedí un número carnal, no te hagas el gracioso")
            print(f"Error: {e}")
        # si todo salio bien terminamos el bucle
        else:
            break
        # Se ejecuta siempre
        finally:
            print("Manejo de excepción finalizado")
    # mostramos el resultado
    return resultado

print(sumar_dos())