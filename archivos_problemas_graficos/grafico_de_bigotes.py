import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("soyDaltoPython\\archivos_problemas_graficos\\bigotes.csv")

# creando el gráfico
sns.boxplot(x="categoria",y="valor",data=df)

# mostrando el gráfico
plt.show()