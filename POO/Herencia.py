class Persona:
    def __init__(self, nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"Hola, me llamo {self.nombre} estoy hablando lol.")
        
        
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        # herencia simple
        super().__init__(nombre,edad,nacionalidad)
        # super es una forma de llamar lo que ocupamos de la clase padre (Persona) para 
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,notas,universidad):
        # herencia simple
        super().__init__(nombre,edad,nacionalidad)
        # super es una forma de llamar lo que ocupamos de la clase padre (Persona) Solo herencia simple 
        self.notas = notas
        self.universidad = universidad
        
class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"

# HERENCIA MULTIPLE
class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        # super() llama a la(s) clase(s) padre
        return f'Hola soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en la {self.empresa}'

angel = EmpleadoArtista("Angel",25,"mexicano","Programador",18000,"Fiscalía")

# print(angel.presentarse())

herencia = issubclass(EmpleadoArtista,Artista) # True
herencia = issubclass(Artista,Persona) # False

instancia = isinstance(angel,EmpleadoArtista) # True
instancia = isinstance(angel,Artista) # True
instancia = isinstance(angel,Persona) # True


angel = Artista("Programar")
instancia = isinstance(angel,Persona) # False
instancia = isinstance(angel,EmpleadoArtista) # False
instancia = isinstance(angel,Artista) # True
print(instancia)