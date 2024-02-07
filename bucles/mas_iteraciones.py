frutas = ["banana", "manzana", "ciruela",
          "pera", "naranja", "granada", "durazno"]
cadena = "Hola Engel"
numeros = [2, 5, 8, 10]

# evitamos que se coma una granada.
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"Me voy a comer una {fruta}")

print("============================================")

# evitamos que el bucle continue
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "perra":
        break
else:
    # lo ejecuta solo si acaba, si se va al break no lo ejecuta.
    print("haaaa me duele la panza")

print("============================================")
for letra in cadena:
    print(letra)

print("============================================")
# for en 1 linea
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
