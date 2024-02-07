animales = ["perro", "gato", "loro", "cocodrilo"]

for animal in animales:
    print(animal)

numeros = []
# numeros = [52, 16, 14, 72]
print("============================================")

for numero in numeros:
    resultado = numero * 2
    print(resultado)

print("============================================")

# iterar 2 o más listas a la ves sin anidar (deben tener la misma longitud las listas)

for numero,animal in zip(numeros,animales):
    print(f"recorriendo la lista 1 y 2 con: {numero} y {animal}")
    
print("============================================")

for num in range(5,10):
    print(num)

print("============================================")

#forma no optima de recorrer una lista (No funciona en conjutos)
# for num in range (len(numeros)):
#     print(f"esta es la forma culera de recorrer la lista: {numeros[num]} como ves, cara de pez")
    
print("============================================")

    
#forma correcta de recorer una lista con su indice
for num in enumerate(numeros):
    print(type(num))
    print(f"con el num en: {num}")
    indice = num[0]
    valor = num[1]
    print(f"el índice es: {indice} y el valor es {valor}")
    
print("============================================")

#forma practica y elegantioso

for i,num in enumerate(numeros):
    print(f"el índice es: {i} y el valor es {num}")
    
print("============================================")

# for-else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor acutal: {numero}")
else:
    print("el bucle acabo")
    
    
# todo lo anterior funciona igual para tuplas, listas y conjuntos