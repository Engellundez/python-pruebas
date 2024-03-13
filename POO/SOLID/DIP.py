# ESTO VIOLA EL PRINCIPIO DE NO DEPENDENCIAS  

# class Diccionario:
#     def verificar_palabra(self,palabra):
#         # Lógica
#         pass
    
# ya que al estar dependiendo de Diccionario, si algo cambia en diccionario, desmadra todo lo que hay aquí 
# haciendo inservible el PRINCIPIÓ
# class CorrectorOrtográfico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_text(self,texto):
#         # Usamos el diccionario para corregir el texto

from abc import ABC, abstractclassmethod

# Esta al ser la clase más importante para esto en especifico 
# es nuestra plantilla principal para los lugares a verificar
class VerificadorOrtográfico(ABC):
    @abstractclassmethod
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras
        pass
    
# Verifica diccionario
class Diccionario(VerificadorOrtográfico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras si está en el diccionario
        pass
    
# Verifica en internet
class ServicioWeb(VerificadorOrtográfico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras si está en el servicio web
        pass
    
# Solicita el servicio web a usar
class CorrectorOrtográfico:
    def __init__(self, verificador):
        self.palabra = 'Holu'
        self.verificador = verificador
        
    def corregir_texto(self):
        # usamos el verificador para corregir texto
        palabra_verificada = self.verificador.verificar_palabra(self.palabra)
        return palabra_verificada
    
    
    
corrector = CorrectorOrtográfico(ServicioWeb())
corrector = CorrectorOrtográfico(Diccionario())