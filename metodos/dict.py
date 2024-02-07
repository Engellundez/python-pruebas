diccionario = {
    "nombre": "Engel",
    "apellido": "Lundez",
    "edad": 24    
}
# Devuelve las claves (también no puede servir para iterar)
claves = diccionario.keys()
# Obtenemos el valor con la key buscada, pero si no lo encuentra regresa un none.
valor_de_nombre = diccionario.get("nombre")

# eliminando un elemento del diccionario
diccionario.pop("edad")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

# eliminando todo del diccionario
# diccionario.clear()

print(diccionario)
print(diccionario_iterable)