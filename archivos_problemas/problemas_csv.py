# cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("soyDaltoPython\\problemas_resueltos\\datos.csv")

# convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

# mostrar el tipo de dato del primer elemento de la columna edad
print(df['edad'][0])

# remplazando los datos "engel" por "El puto amo "
df['nombre'].replace("engel","El puto amo",inplace=True)

# Eliminando las filas con datos faltantes, columnas con datos faltantes seria dropna(axis=1)
df = df.dropna()

# Eliminando las filas repetidas
df = df.drop_duplicates()


# creando un CSV con el dataframe resultante (limpio)
df.to_csv("soyDaltoPython\\problemas_resueltos\\datos_limpios.csv")
