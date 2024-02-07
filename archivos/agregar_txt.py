with open("soyDaltoPython\\archivos\\texto.txt", "a", encoding="UTF-8") as archivo:
    # agregando texto al archivo
    archivo.write("\n\nhaaaaaaaaaaa no mms")
    
with open("soyDaltoPython\\archivos\\texto.txt", encoding="UTF-8") as archivo:
    print(archivo.read())