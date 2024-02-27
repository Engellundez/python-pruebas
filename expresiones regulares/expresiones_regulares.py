import re
texto = '''Holabab maestro. esta es la cadena 1. como estas mi capitan
Esta es la linea 225654 linea de texto. 
y Esta la final (linea 3) definitiva mi capitan'''

# HACIENDO BUSQUEDAS SIMPLES
# result = re.search("Hola", texto)
# result = re.findall("Esta", texto, re.IGNORECASE)

# \d -> busca SOLO dígitos numéricos del 0 - 9
# result = re.findall(r"\d", texto)

# \D -> busca TODO MENOS dígitos numéricos del 0 - 9
# result = re.findall(r"\D", texto)

# \w -> busca SOLO caracteres alfanuméricos [a-z A-Z 0-9 _]
# result = re.findall(r"\w", texto)

# \W -> busca TODO MENOS caracteres alfanuméricos [a-z A-Z 0-9 _]
# result = re.findall(r"\W", texto)

# \s -> busca SOLO espacios en blanco -> espacios, tabs, saltos de linea
# result = re.findall(r"\s", texto)

# \S -> busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
# result = re.findall(r"\S", texto)

# . -> busca TODO MENOS saltos en linea
# result = re.findall(r".", texto)

# \n -> busca SOLO saltos en linea
# result = re.findall(r"\n", texto)


# \ -> cancelamos caracteres especiales, cancelando la función del punto y buscando puntos
# result = re.findall(r"\.", texto)

# armando una cadena que busque un numero, seguido de un punto y un espacio
# result = re.findall(r'\d\.\s', texto)


# ^ Busca el comienzo de una linea
# re.M activa la multilinea
# result = re.findall(r"^Esta", texto, re.M)

# $ -> busca el final de una linea
# result = re.findall(r"capitan$", texto, re.M)

# {n} -> busca n cantidad de veces el valor de la izquierda
# result = re.findall(r"\d{3}\s",texto)

# {n,m} -> al menos n, como máximo m
result = re.findall(r'(ab){2,4}', texto)
print(result)