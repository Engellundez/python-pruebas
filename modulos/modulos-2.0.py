# IMPORTAMOS DESDE UNA CARPETA DENTRO
import funciones_buenas.saludar as saludar

print(saludar.saludar("Lucas"))
# IMPORTAMOS DESDE UNA CARPETA ATRAS O AFUERA

import sys

# print(sys)
# print(sys.builtin_module_names)
# print(sys.path)

sys.path.append("C:\\inetpub\\wwwroot\\python\\soyDaltoPython\\funciones_buenas")

# print(sys.path)

import saludar as s
print(s.saludar_raro("Engel"))