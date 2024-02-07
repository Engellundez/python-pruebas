diccionario = {
        "nombre": "engel",
        "apellido": "Lundez",
        "subs" : 0,
    }

#obtenemos solo las claves
for key in diccionario:
    print(key)
    
print("============================================")
    
# obtenemos las claves y sus valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es {key}, y el valor es: {value}")