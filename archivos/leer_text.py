# usando open para abrir un archivo.
archivo_sin_leer = open("soyDaltoPython\\archivos\\texto.txt",encoding="UTF-8")

# Leer archivo completo
# archivo = archivo_sin_leer.read()
# print(archivo)

# el archivo no se puede leer más de 1 ves por cuestiones de seguridad. 

# Leer archivos linea x linea
# lineas = archivo_sin_leer.readlines()
# print(lineas)

# leer una sola linea
linea = archivo_sin_leer.readline()
print(linea)

# esto hay que cerrarlo para la propia la ram, o limitar la cantidad de veces que tiene
archivo_sin_leer.close()

# una vez que se cierra ya no se puede usar, solo abrirlo con open() de nuevo