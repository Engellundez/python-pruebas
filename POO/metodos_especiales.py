# son funciones que tiene un nombre especial resrvado, inicia y terminan con 2 guiones bajos __Name__

class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    # Definimos que se va a mostrar cuando se llame al puro objeto, sin esto el programa solo mandara 
    # <__main__.Persona object at 0x0000017C6AF68FB0>
    def __str__(self):
        return f'Persona(nombre={self.nombre},edad={self.edad})'
    
    # Funciona igual que el String de arriba pero como representacion de datos
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)
    
angel = Persona("Angel", 25)

repre = repr(angel) # accedemos a la interpretación del objeto
resultado = eval(repre) # Generamos la representación del objeto para usar la variable como tal.

print("resultado",resultado)
print("nombre",resultado.nombre)
print("edad",resultado.edad)
print(repre)


# ARITMETICOS
# __add__(self, other): sobrecarga del operador de suma (+)
# __sub__(self, other): sobrecarga del operador de resta (-)
# __mul__(self, other): sobrecarga del operador de multiplicación (*)
# __div__(self, other): sobrecarga del operador de división (/)
# __mod__(self, other): sobrecarga del operador de módulo (%)
# __pow__(self, other): sobrecarga del operador de exponenciación (**)

# COMPARACIÓN
# __eq__(self, other): sobrecarga del operador de igualdad (==)
# __ne__(self, other): sobrecarga del operador de desigualdad (!=)
# __lt__(self, other): sobrecarga del operador de menor que (<)
# __gt__(self, other): sobrecarga del operador de mayor que (>)
# __le__(self, other): sobrecarga del operador de menor o igual que (<=)
# __ge__(self, other): sobrecarga del operador de mayor o igual que (>=)

# ASIGNACIÓN
# __iadd__(self, other): sobrecarga del operador de suma en asignación (+=)
# __isub__(self, other): sobrecarga del operador de resta en asignación (-=)
# __imul__(self, other): sobrecarga del operador de multiplicación en asignación (*=)
# __idiv__(self, other): sobrecarga del operador de division en asignación (/=)
# __imod__(self, other): sobrecarga del operador de módulo en asignación (%=)
# __ipow__(self, other): sobrecarga del operador de exponenciación en asignación (**=)

# OTROS
# __str__(self): sobrecarga del operador str(). Devuelve una representación legible como cadena del objeto.
# __len__(self): sobrecarga del operador len(). Devuelve la longitud del objeto.
# __getitem__(self, index): sobrecarga del operador de indexación ([]). Permite acceder a elementos del objeto por indice.


# SOBRECARGA DE OPERADORES.
pedro = Persona("Pedro", 20)
maria = Persona("maria", 20)
resultado = pedro + angel + maria
print(resultado)
print(resultado.edad)
print(resultado.nombre)