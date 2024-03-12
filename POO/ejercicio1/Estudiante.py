class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando.")
        

        
nombre = input("Por favor ingresa el nombre del estudiante: ")
edad = input("Por favor ingresa la edad del estudiante: ")
grado = input("Por favor ingresa el grado al que asiste el estudiante: ")


estudiante = Estudiante(nombre,edad,grado)
print(f"""
      DATOS DEL ESTUDIANTE \n \n
      Nombre: {estudiante.nombre} \n
      edad: {estudiante.edad} \n
      grado: {estudiante.grado} \n
      """)

while True:
    estudiar = input("hacemos que haga algo como 'estudiar' ? ")
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        break
    