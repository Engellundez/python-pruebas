numeros = [4, 7, 1, 42, 15]

# encontrando el mayor de una lista

numero_mas_alto = max(numeros)  # onlyNum
print(numero_mas_alto)

print("============================================")

numero_mas_bajo = min(numeros)  # onlyNum
print(numero_mas_bajo)
print("============================================")

# redondeando a 6 decimales
# antes
numero = round(12.345678 * 100)
print(numero / 100)

# ahora
numero = round(12.345678, 2)
print(numero)

print("============================================")

# retorna False -> 0,vacío, False, ninguno
resultado_bool = bool(0)
print(resultado_bool)
print("============================================")

# retorna True, si todos los valores son verdaderos
resultado_all = all([234, "true", [344, False], "False"])
print(resultado_all)
print("============================================")

#suma todos los valores de un iterable

suma_total = sum(numeros) # onlyNum
print(suma_total)