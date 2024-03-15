# Importamos datos de voz que va a responder
import pyttsx3 as hablar
# puede escribir o hacer varias cosas en el sistema
# ocupa a Pillow para funcionar.
import pyautogui as gui

import SpeechRecognition

sabina = hablar.init()

sabina.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
sabina.setProperty('rate', 170)
sabina.say('Me vale verga perro, y abrace a la verga hijo de su puta medre, me vale verga a la verga')
sabina.runAndWait()
gui.write('Hola vamos a responder')
