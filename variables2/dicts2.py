#creando diccionarios con dict()
dicionario = dict(nombre="engel",apellido="lundez") 

# las listas no pueden ser claves porque son mutables
# dicionario = {["dalto","rancio"]:"jajas"} #Error

#creando diccionario con fromkeys(), y sin definir
dicionario = dict.fromkeys(["nombre","apellido"]) # (iterable, valor.)

print (dicionario)

