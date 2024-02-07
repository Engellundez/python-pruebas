# Creando una lista con list()
lista = list(["hola","mi","amigo"])

canti_elementos = len(lista)
# agrega un elemento a la lista
lista.append("jajajajaja")

# agrega un elemento en un indice en especifico sin remplazar elementos
lista.insert(2,"toma maaaa")

# agregando una lista en otra lista
lista.extend(["una lista nueva", "2024"])

# elimina un elemento por su indice (con -n eliminamos al revés el indice comenzando con 1)
lista.pop(2)

# elimina el elemento con el valor dado, si no existe el valor da una excepción
lista.remove("2024")

# Pone la lista al revés, el primer elemento es el ultimo y asi subsecuentemente
lista.reverse()

# Ordena la lista ascendente (solo si son string, si no da error, Si es numérico y booleano ordena primero los False después los True y después el ordenamiento Numérico.)
lista.sort()

# elimina la lista
lista.clear()