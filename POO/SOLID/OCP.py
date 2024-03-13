# Principio Abierto Cerrado
# Abierto a las Exenciones pero Cerrado a las modificaciones
class Notificado:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError

# Extienden de Notificado pero no modifico Notificado
class NotificadoEmail(Notificado):
    def notificar(self):
        print(f"Enviando mensaje por EMAIL a {self.usuario.email}")


class NotificadoSms(Notificado):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.email}")