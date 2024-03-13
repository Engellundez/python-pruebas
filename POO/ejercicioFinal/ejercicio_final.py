# from textblob import TextBlob


# class AnalizadorDeSentimientos:
#     def analizar_sentimiento(self, texto):
#         análisis = TextBlob(texto)
        
#         if(análisis.sentiment.polarity > 0):
#             return "positivo"
#         elif análisis.sentiment.polarity == 0:
#             return "neutro"
#         else:
#             return "negativo"
        

# analizador = AnalizadorDeSentimientos()
# resultado = analizador.analizar_sentimiento("hi")

# print(resultado)


import openai

# NO JALA PORQUE CUESTA :(
openai.api_key = "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"
# EL ROL DEL SISTEMA PARA EL OPEN AI
system_rol = '''Hace de cuenta que sos un analizador de sentimientos.
                Yo te paso sentimientos y vos analizas el sentimiento de los 
                mensajes y me das una respuesta con al menos 1 carácter y como máximo 4 caracteres
                SOLO RESPUESTAS NUMÉRICAS. donde -1 es negatividad máxima, 0 es neutral y 1 es positividad máxima.
                puedes ir entre esos rangos, es decir 0.3, -0.5 etc también son válidos.
                (Puedes responder solo con ints o floats)'''
                
mensajes = [{"role": "system", "content": system_rol}]

class AnalizadorDeSentimientos:
    def analizador_sentimiento(self,polaridad):
        if polaridad <= -0.7:
            return "\x1b[1;31m" + "Muy negativo"
        elif polaridad > -0.6 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo"
        elif polaridad > -0.3 and polaridad <= -0.1:
            return "\x1b[1;31m" + "Algo negativo"
        elif polaridad > -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutro"
        elif polaridad > 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo"
        elif polaridad > 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy positivo"
        
analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\nDime algo: "+" \x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= mensajes, 
        max_tokens = 8
    )
    
    respuesta_chat = completion.choices[0].message["content"]
    mensajes.append({"role": "assistant", "content": respuesta_chat})
    
    sentimiento = analizador.analizador_sentimiento(float(respuesta_chat))