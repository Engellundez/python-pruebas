# función simple
def saludar(nombre, sexo="hombre"):
    sexo = sexo.lower()
    if(sexo=="mujer"):
        adjetivo= "reina"
    elif(sexo=="hombre"):
        adjetivo="titan"
    else:
        adjetivo="amor"
    
    print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")


# ejecutar
saludar("Engel")
saludar("Rodrigo","Pez")
saludar("Daniela","Mujer")


# función que retorne valores

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
    
    
password,primer_numero = crear_contraseña_random(398)
print (f"tu contra nueva es: {password}")
print (f"numero clave: {primer_numero}")
    