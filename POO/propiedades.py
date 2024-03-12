# PROPERTY como Setters, Getters o Deleter

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad

    # Transforma la función para que sea llamada como un atributo y no como funcion 
    @property
    def nombre(self):
        return self.__nombre 
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    # Elimina el parametro de la memoria y restringe el acceso posterior.
    @nombre.deleter
    def nombre(self):
        del self.__nombre 

angel = Persona("Angel", 25)

# Una llamda más facíl a traves de la funcion pero invocandola como propiedad.
nombre = angel.nombre
print(nombre)

# Esto tira error porque es un getter, no un setter entonces es complicado renombrar y más facil proteger los datos agregados.
# angel.nombre = "Lucas"


# Aqui ya no tira error porque ya existe el  @nombre.setter
angel.nombre = "Lucas"

nombre = angel.nombre
print(nombre)

# eliminar si existe un @---.deleter
del angel.nombre

