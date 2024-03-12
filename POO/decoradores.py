def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar la funcion")
        funcion()
        print("Despues de llamar")
    
    return funcion_modificada

# SIN DECORADOR

# def saludo():
#     print("hola Engel")

# saludo_modificado = decorador(saludo)
# saludo_modificado()


# CON DECORADOR
# SE DECLARA CON @ LA FUNCION SE DECORA CON UNA FUNCION EN ESPECIFICA
@decorador
def saludo():
    print("hola Engel")
    
saludo()