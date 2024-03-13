# class Ave:
#     def volar(self):
#         return "Estoy Volando"
    
# class Pingüino(Ave):
#     def volar(self):
#         return "Yo no puedo volar"
    

# def hacer_volar(ave = Ave):
#     return ave.volar()

# print(hacer_volar(Pingüino()))

# ESTA ES LA CLASE BASE
class Ave:
    pass

# las aves voladoras deben poder hacer todo lo que tiene AVE y no sobreescribir como en el anterior ejemplo
class AveVoladora(Ave):
    def volar(self):
        return 'Estoy volando'
    
# y aqui puede recibir sus propios metodos de no volador.
class AveNoVoladora(Ave):
    pass

# AQUI APLICA
gorreon = AveVoladora()
pingüino = AveNoVoladora()