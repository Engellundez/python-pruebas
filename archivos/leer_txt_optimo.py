# abriendo el archivo con with open
with open("soyDaltoPython\\archivos\\texto.txt", encoding="UTF-8") as archivo:
    print("hola")
    print(archivo.read())
    
# no es necesario cerrarlo con el with open