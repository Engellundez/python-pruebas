class Pato:
    def parpar(self): 
        print ("Cuac!")
    def plumas(self): 
        print ("El pato tiene plumas blancas y grises.")
 
class Persona:
    def parpar(self):
        print ("La persona imita el sonido de un pato.")
    def plumas(self): 
        print ("La persona toma una pluma del suelo y la muestra.")
 
def en_el_bosque(pato):
    pato.parpar()
    pato.plumas()
 
def juego():
    donald = Pato()
    juan = Persona()
    en_el_bosque(donald)
    en_el_bosque(juan)

juego()