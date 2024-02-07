cadena1 = "Hola soy Engel. aqui entra otro dato perro"
cadena2 = "Bienvenido maquinola"

# dir(cadena1) # devuelve los métodos que podemos usar dependiendo del tipo de dato que se usa

# DATO.MÉTODO(PARÁMETRO)
mayus = cadena1.upper()
minus = cadena1.lower()
primer_letra_mayus = cadena1.capitalize()

buscar_en_cadena = cadena1.find("Hola") # Regresa index | -1
buscar_index = cadena1.index("E") # excepción si no encuentra coincidencia

es_numerico = cadena1.isnumeric() # sin importar el tipo de dato, si es numérico regresa True
es_alfanumerico = cadena1.isalpha()

contar_coincidencias = cadena1.count('Hola')
contar_caracteres = len(cadena1)

empieza_con = cadena1.startswith("Hol")
termina_con = cadena1.endswith("el")

remplazamos_caracteres_buscados = cadena1.replace('la', 'lu')
lista_a_partir_de_una_cadena = cadena1.split('.')
