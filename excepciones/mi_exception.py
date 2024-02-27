# creando mi propia excepción personaliza
class MiException(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")

# Lanzando mi propia excepción
# raise MiException("Jjajaja, persona poco culta")

# manejando la
try:        
    raise MiException("Jajajaja, persona poco culta")
except:
    print("como vas a cometer ese error?")

