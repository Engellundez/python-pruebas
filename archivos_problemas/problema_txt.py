# 2 listas, una con nombres y otra con apellidos

nombres = ["Lucas","Matias","Engel","Camilo","Ter","Mei","Jovanna"]
apellidos = ["Dalto","Zing","Lundez","Septimo","Martinez","Ruiz","Lopez"]

# Registrar esta información en un TXT de forma óptima

with open("soyDaltoPython\\problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n---------------°\n") for n,a in zip(nombres,apellidos)]