import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("soyDaltoPython\\archivos_problemas_graficos\\cofla_ingresos.csv")

# creando el gráfico
sns.barplot(x="fuente",y="ingresos",data=df)

# obteniendo el total
total_ingresos = df['ingresos'].sum()

# mostrando el total
print(total_ingresos)

# mostrando el gráfico
plt.show()