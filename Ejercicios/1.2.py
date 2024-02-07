ejercicio = """
a.- pedirle al usuario que diga un texto real y:
    * calcular cuanto tardaría en decir esa frase
    * ¿Cuantas palabras dijo?

b.- sitarda más de 1 minuto:
    * decirle: "para flaco tampoco te pedí un testamento".
    
c.- Dalto habla un 30% más rápido:
    *¿Cuanto tardaría él en decirlo?
"""

palabras_x_segundo = 2
frase = input("Dame un texto real y no tus guarrerias, y te calculo cuanto tardarias en decirlo: ") # Que haces maestro que contas
palabras_separadas = frase.split(" ")
canti_palabras = len(palabras_separadas)
segundos_x_frase = round(canti_palabras / palabras_x_segundo,2) 

print(f"tardaria en decir esa frase {segundos_x_frase} segundos")#19
print(f"la cantidad de palabras que nos diste es de {canti_palabras} palabras")#38

if segundos_x_frase > 120:
    print("para flaco tampoco te pedí un testamento")
    
palabras_dalto = palabras_x_segundo * 1.3
segundos_x_frase_dalto = round(canti_palabras / palabras_dalto,2) 
print(f"Dalto tardaria en decir esa frase {segundos_x_frase_dalto} segundos")#14.61

