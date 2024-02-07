# Declaramos funciones anonimas y se almacenan en una funcionvar. Solo para funciones simples. 
multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(8))

print("=====================================================")

numeros = [1,2,3,4,5,6,7,8,9]

def es_par(num):
    if (num%2==0):
        return True
    
    return False

numeros_pares = filter(es_par,numeros)

print(list(numeros_pares))

print("=====================================================")

#ejecutando lo mismo con lambda

numeros_pares = filter(lambda numero: numero%2 == 0, numeros)
print(list(numeros_pares))