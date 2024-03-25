class Personaje:
    def __init__(self, nombre = "Default", fuerza = 0, inteligencia = 0, defensa =0, vida=0):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    
    def __repr__(self) -> str:
        return f'''nombre: {self.__nombre}
    - vida: {self.__vida}
    - inteligencia: {self.__inteligencia}
    - fuerza: {self.__fuerza}
    - defensa: {self.__defensa}'''
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
    
    @property
    def esta_vivo(self):
        return self.__vida > 0
    
    def __morir(self):
        self.__vida = 0
        print(self.__nombre, 'ha muerto')
    
    def __daño(self, enemigo):
        return self.__fuerza - enemigo._Personaje__defensa
    
    def atacar(self, enemigo):
        daño = self.__daño(enemigo)
        enemigo._Personaje__vida = enemigo._Personaje__vida - daño
        print(f'{self.__nombre} ha realizado {daño} puntos de daño a {enemigo._Personaje__nombre}')
        if enemigo.esta_vivo:
            print(f'La vida de {enemigo._Personaje__nombre} es {enemigo._Personaje__vida}')
        else:
            enemigo.__morir()

# PYTHON TODO ES PUBLICO, SOLO HAY QUE SABERLO LLAMAR
mi_personaje = Personaje('BitBoss', 10,1,5,100)
mi_enemigo = Personaje('Enemy Stando', 8,5,3,5)
mi_enemigo.atacar(mi_personaje)
mi_personaje.atacar(mi_enemigo)
print(mi_enemigo)
print(mi_personaje)