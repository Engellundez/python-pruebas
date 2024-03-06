import re
texto = '''Holabab maestro. esta es la cadena 1. como estas mi capitan
Esta es la linea 2256545 linea de texto.  150057 abababab
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

# {n,m} -> al menos n coincidencias, m como máximo de coincidencias
# result = re.findall(r'\d{1,5}', texto) # va a tomar la cantidad máxima de la búsqueda, aunque tenga más números ya que esto lo filtrara y dividirá.

# (g){n} -> busca un grupo que se repita n veces 
# (g){2} => 'gg gg' y devuelve solo ['g','g']
# (g1){2} => 'g1g1 g1g1' y devuelve solo ['g1','g1']
# result = re.findall(r'(ab){2}', texto)

# [se]{n} -> busca una serie que se repita n veces 's' y 'e' y sus posibles 
# aa,ab,ba,bb | ss se es ee
# result = re.findall(r'[ab]{2}', texto) 

# | -> busca una cosa o la otra
result = re.findall(r'\d{2,4}|Hola', texto)
print(result)