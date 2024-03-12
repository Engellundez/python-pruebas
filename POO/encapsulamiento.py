class MiClase:
    def __init__(self):
        # Para poner un atributo como privado solo basta poner __ al inicio para que sea privado
        self.__atributo_privado = "Valor" 
        
    def __hablar(self):
        print("hola, como estás")
        
objeto = MiClase()

# mada un error por ser un atributo privado
# print(objeto.__atributo_privado)

# Como podemos obtener los atributos privados?
# vamos a utilizar geter o seter


class Persona:
    def __init__(self,nombre,edad):
        # Valor muy privado
        self.__nombre = nombre
        # Valor privado
        self._edad = edad
    
    # Getter
    def get_nombre(self):
        return self.__nombre
    
    # Setter
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
# Instanciando la clase
angel = Persona("Angel Lundez", 25)

# Obtenemos e imprimimos
nombre = angel.get_nombre()
print(nombre)

# actualizamos los datos 
angel.set_nombre("Luis")
nombre = angel.get_nombre()
print(nombre)


# AHORA USAMOS LOS DECORADORES PROPERTY, O FUNCIONES QUE USAN PYTHON PARA SIMPLIFICAR ESTO

