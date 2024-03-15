from abc import ABC, abstractclassmethod
from textblob import TextBlob
import openai
import random

class Sentimiento:
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
        
    def __str__(self):
        return "\x1b[1;{}m{} \x1b[0;37m".format(self.color,self.nombre)

class VerificadorSentimientos(ABC):
    @abstractclassmethod
    def analizar(self, texto):
        pass

class VerificaOpenAi(VerificadorSentimientos):
    # NO JALA PORQUE CUESTA :(
    # EL ROL DEL SISTEMA PARA EL OPEN AI
    def __init__(self):
        self.system_rol = '''Hace de cuenta que sos un analizador de sentimientos.
                Yo te paso sentimientos y vos analizas el sentimiento de los 
                mensajes y me das una respuesta con al menos 1 carácter y como máximo 4 caracteres
                SOLO RESPUESTAS NUMÉRICAS. donde -1 es negatividad máxima, 0 es neutral y 1 es positividad máxima.
                puedes ir entre esos rangos, es decir 0.3, -0.5 etc también son válidos.
                (Puedes responder solo con ints o floats)'''
        openai.api_key = "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"
        self.mensajes = [{"role": "system", "content": self.system_rol}]
        
    def analizar(self, user_prompt):
        self.mensajes.append({"role": "user", "content": user_prompt})
        self.respuesta_bot()
        
    def respuesta_bot(self):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages= self.mensajes, 
            max_tokens = 8
        )
        respuesta_chat = completion.choices[0].message["content"]
        self.mensajes.append({"role": "assistant", "content": respuesta_chat})
        
        return float(respuesta_chat)

class VerificaTextBlob(VerificadorSentimientos):
    def analizar(self, texto):
        resultado = TextBlob(texto)
        return resultado.sentiment.polarity
    
class VerificaRandom(VerificadorSentimientos):
    def analizar(self, texto):
        # el texto me vale carnal, lo importante es tener fé
        resultado = random.uniform(-1,1)
        return resultado

class AnalizadorDeSentimientos:
    def __init__(self,rangos, verificador_sentimientos):
        self.rangos = rangos
        self.verificador_sentimientos = verificador_sentimientos
    
    def analizador_sentimiento(self,palabra):
        valor = self.verificador_sentimientos.analizar(palabra)
        return self.calcular_sentimiento(valor)
    
    def calcular_sentimiento(self,polaridad):
        for rango, sentimiento in self.rangos:
            if (rango[0] < polaridad <= rango[1]):
                return sentimiento
        
        return Sentimiento("Muy negativo", "31")

rangos = [
    ((-1,-0.6), Sentimiento("Muy negativo", "31")),
    ((-0.6,-0.3), Sentimiento("Negativo", "31")),
    ((-0.3,-0.1), Sentimiento("Algo negativo", "31")),
    ((-0.1,0.1), Sentimiento("Neutral", "33")),
    ((0.1,0.3), Sentimiento("Algo positivo", "32")),
    ((0.3,0.6), Sentimiento("Positivo", "32")),
    ((0.6,1), Sentimiento("Muy positivo", "32"))
]

analizador = AnalizadorDeSentimientos(rangos,VerificaTextBlob())
# analizador = AnalizadorDeSentimientos(rangos,VerificaRandom())

# if __name__ == '__main__':
while True:
    texto = input("\x1b[1;33m" + "\nDime algo: "+" \x1b[0;37m")
    sentimiento = analizador.analizador_sentimiento(texto)
    print(sentimiento)
    