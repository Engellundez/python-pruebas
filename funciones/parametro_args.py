# No optima de sumar valores

# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados += numero
#     return numeros_sumados

# res = suma([5,2,9,5])

# Usando el operador * como argumento (*args) (no se pueden agregar más argumentos después del args porque ya no lo detecta.)

def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus números es: {sum(numeros)}"


res = suma("Ricardio", 5, 2, 9, 5)
print(res)
