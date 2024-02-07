#creando un conjunto con set()
conjunto = set(["dato1","dato2", ("datoenlista1","datoenlista2")])

#metiendo un conjunto dentro de otro
conjunto1 = frozenset({"dato 1", "dato 2"})
conjunto2 = {conjunto1, "dato 3"}

print(conjunto2)

# TEORIA DE CONJUNTOS

conjunto1 = {1,3,5,7}
# conjunto2 = {1,3,7}
conjunto2 = {8,2,4,6}

resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

# verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)