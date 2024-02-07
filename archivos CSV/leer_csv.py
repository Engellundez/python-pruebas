# FORMA NORMAL SIN LIBRERIAS
# with open("soyDaltoPython\\Archivos CSV\\datos.csv") as archivo:
#     print(archivo.read())

# PAQUETE PROPIO DE PYTHON CSV (LIMITADO DE FORMA BASE)
# =====================================================================================================================================
# import csv

# with open("soyDaltoPython\\Archivos CSV\\datos.csv") as archivo:
#     reader = csv.reader(archivo)
#     for row in reader:
#         print(row)
        
# IMPORTAR CSV CON PANDAS
# =====================================================================================================================================
# descargamos la libreeria pandas con el comando py -m pip install pandas (para trabajar archivos CSV con más opciones)

import pandas as pd #PD ES LA ABREVIATURA COMÚN PARA ESTE LIB

# df = pd.read_csv("soyDaltoPython\\archivos CSV\\datos.csv",names=["name","agrega","fila"]) # df = dataFrame
df = pd.read_csv("soyDaltoPython\\archivos CSV\\datos.csv")
df2 = pd.read_csv("soyDaltoPython\\archivos CSV\\datos.csv")

# OBTENER COLUMNA NOMBRE
nombres = df["nombre"]
# print(nombres)
# ordenando por edad
df_ordenado = df.sort_values("edad")

# print(df)
# print("==================================================================================================================================================")
# print(df_ordenado)

# ordenandolo de forma descendente
df_ordenado_desc = df.sort_values("edad",ascending=False)
# print(df_ordenado_desc)

# CONCATENANDO 2 DATAFRAMES
df_concatenado = pd.concat([df,df2])
print(df_concatenado)
print("==================================================================================================================================================")

# accediendo a las primeras 3 fila con head(3)
primeras_filas= df.head(3)
print(primeras_filas)
print("==================================================================================================================================================")

# accediendo a las ultimas 3 fila con tail(3)
ultimas_filas= df.tail(3)
print(ultimas_filas)
print("==================================================================================================================================================")

# accediendo a la cantidad de filas y columnas con shape 
# filas_y_columnas_totales= df.shape
filas_totales, columnas_totales = df.shape
print(f"la filas totales son {filas_totales} y las columnas de estas son {columnas_totales}")
print("==================================================================================================================================================")

# obteniendo data estadística del dataframe
df_info= df.describe()
print(df_info)
print("==================================================================================================================================================")

# accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[3,"edad"]
print(elemento_especifico_loc)
print("==================================================================================================================================================")

# accediendo a un elemento especifico del df con iloc
elemento_especifico_loc = df.iloc[2,2]
print(elemento_especifico_loc)
print("==================================================================================================================================================")

# accediendo a todas las filas de una columna con loc
apellidos = df.loc[:,"nombre"]
print(apellidos)
print("==================================================================================================================================================")

# accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]
print(apellidos)
print("==================================================================================================================================================")

# accediendo a todos los datos de la fila con loc
fila3 = df.loc[2,:]
print(fila3)
print("==================================================================================================================================================")

# accediendo a todos los datos de la fila con iloc
fila3 = df.iloc[0,:]
print(fila3)
print("==================================================================================================================================================")

# accediendo a filas > 30
mayor_que_30 = df.loc[df["edad"]>30,:]
print(mayor_que_30)
print("==================================================================================================================================================")

# accediendo a filas < 30
menor_que_30 = df.loc[df["edad"]<30,:]
print(menor_que_30)
print("==================================================================================================================================================")


# =====================================================================================================================================
# SLICING : PARA LISTAR DATOS
# cadena = "0123456789"
# print(cadena[2:8])
