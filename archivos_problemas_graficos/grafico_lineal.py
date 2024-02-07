import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("soyDaltoPython\\archivos_problemas_graficos\\pedos.csv")

# creando el gráfico
sns.lineplot(x="fecha",y="pedos",data=df)

# poniendo un punto en el gráfico
plt.plot("09-01-24",17,"o")

# mostrando el gráfico
plt.show()