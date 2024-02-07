# creando una funcion que nos devuelva los numeros primos

def es_primo(num):
    for i in range(2, num-1):
        if num % i == 0:
            return False
        
    return True

def primos_hasta(num):
    primos = [1]
    for i in range(3, num+1):
        resultado = es_primo(i)
        if resultado : primos.append(i)
    return primos

resultado = primos_hasta(50)
print(resultado)

print("=====================================================")

#codigo igual pero en 1 linea

primos_hasta = lambda num : list(filter(lambda x: all(x%i != 0 for i in range(2, int(x**0.5)+1)), range(3,num)))

print(primos_hasta(50))