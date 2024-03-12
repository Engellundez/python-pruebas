# MRO => Method Resolution Order

class A:
    def hablar(self):
        print("hola desde A")

class B(A):
    def hablar(self):
        print("hola desde B")

class C(A):
    def hablar(self):
        print("hola desde C")


class D(B,C):
    pass

class F:
    def hablar(self):
        print("hola desde F")

class E(B, F):
    pass

d = D()

d.hablar()

# busca por niveles, entonces D va y busca el método en la primera clase que encuentra (B) y si no encuentra el 
# método busca en toda la rama de (B), y por ultimo en toda la rama de (C) 

# pero si ambas clases heredan de A va a buscar en B y luego en C y al fina baja a A

# podemos visualizar el mro para ver la ejecución

print(D.mro())
print(E.mro())

F.hablar(d)