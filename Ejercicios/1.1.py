ejercicio = """
el timing para ver los conceptos vistos en python en un curso de corrido es de 2.5 horas como mínimo, 7 horas como máximo y 4 horas en promedio. Este curso lo logro en 1.5 horas

a.- diferencia en porcentaje entre el curso actual y:
    * el más rápido de otros cursos
    * el más lento de otros cursos
    * el promedio de los cursos
    
b.- porcentaje de material inservible que se produce en:
    * el promedio de los cursos
    * el curso actual
    
c.- ver 10 horas de este curso ¿A cuantas de otros cursos equivale? ¿Y al revés?
"""

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
curso_actual = 1.5

# Diferencia de duracion
diferencia_con_min = 100 - round(curso_actual / otros_cursos_min * 100,2) # debe dar 40%
diferencia_con_max = 100 - round(curso_actual / otros_cursos_max* 100,2) # 78.57
diferencia_con_prom = 100 - round(curso_actual / otros_cursos_prom * 100,2) # 62.5
print ('---------------')
print (f"Nuestro curso dura un {diferencia_con_min}% menos que el más rápido")
print (f"Nuestro curso dura un {diferencia_con_max}% menos que el más lento")
print (f"Nuestro curso dura un {diferencia_con_prom}% menos que el promedio")

crudo_promedio = 5
crudo_actual = 3.5

diferencia_crudo_prom = 100 - round(otros_cursos_prom / crudo_promedio * 100,2)#20
diferencia_crudo_act = 100 - round(curso_actual / crudo_actual * 100,2)#57.2

print ('---------------')
print (f"El crudo promedio elimina un {diferencia_crudo_prom}% del tiempo vacío.")
print (f"Nuestro crudo elimina un {diferencia_crudo_act}% del tiempo vacío.")

print ('---------------')
print(f"Ver 10 horas de este curso equivale a ver {round(otros_cursos_prom / curso_actual * 10,2) } horas de otros cursos")#26.6
print(f"Ver 10 horas de otros curso equivale a ver {round(curso_actual / otros_cursos_prom * 10,2) } horas de otros cursos")#3.7
print ('---------------')
