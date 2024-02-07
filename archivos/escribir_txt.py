with open("soyDaltoPython\\archivos\\texto.txt", "w", encoding="UTF-8") as archivo:
    # sobre escribe el archivo
    # archivo.write("haaaaaaaaaaa no mms")
    
    # sobre escribe pero writelines es acumulable
    archivo.writelines(["hola paaaaaa como andas","\n","Texto"])
    archivo.writelines(["asdfas dfs \n","\n","Misericordia divina"])
    
with open("soyDaltoPython\\archivos\\texto.txt", encoding="UTF-8") as archivo:
    print(archivo.read())