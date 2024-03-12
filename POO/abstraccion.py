class Auto():
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "encendidio"
        print(f"El auto está {self._estado}")
    
    def conducir(self):
        if(self._estado == "apagado"):
            self.encender()
        
        print("Conducinendo el auto")


mi_auto = Auto()
mi_auto.conducir()