import speech_recognition as sr
import subprocess as sub
import pyautogui as auto
import pyttsx3 as voz
from time import sleep
import webbrowser as wb

def set_sabina():
    sabina = voz.init()
    velocidad = sabina.getProperty('rate')
    sabina.setProperty('rate', velocidad-25)
    sabina.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
    return sabina

def say_sabina(text):
    sabina = set_sabina()
    sabina.say(text)
    sabina.runAndWait()
    del sabina
    
def interpretar(comando_de_audio_interpretar):
    print(f'Escuche: {comando_de_audio_interpretar}')
    say_sabina(f'Escuche: {comando_de_audio_interpretar}')
    comando_de_audio = comando_de_audio_interpretar.split(' ')
    # palabra_clave_video = ['video', 'reproduce']
    palabra_clave_notepad = ['texto', 'palabra', 'escribir']
    
    # HACEN LO MISMO PERO CON LÓGICA INTERESANTE
    # 1.- Comprobando si alguna palabra clave está en comando_de_audio usando intersección de conjuntos
    comando_de_audio_tokenized = set(comando_de_audio_interpretar.split())
    palabra_clave_video_tokenized = {'video', 'reproduce'}
    
    ver_video = any(palabra_clave_video_tokenized & comando_de_audio_tokenized)
    
    
    # 2.- Itera todas las palabras y regresa el primer True que encuentre si no False
    # ver_video = any(palabra in comando_de_audio for palabra in palabra_clave_video)
    
    # 3.- lógica  pedorra del antiguo mundo  
    # ver_video = False
    # for palabra in palabra_clave_video:
    #     if(palabra in comando_de_audio):
    #         ver_video = True
    #         break
    
    escribir = any(palabra in comando_de_audio for palabra in palabra_clave_notepad)
    
    say_sabina('procesando...')
    print('procesando...',ver_video,escribir)
    
    if ver_video is True:
        abrir_navegador()
    elif escribir is True:
        abrir_blocNotas()

def abrir_blocNotas():
    sub.call('start notepad.exe', shell=True)
    sleep(2)
    texto = 'Estoy listo para escribir tu texto'
    auto.write(texto)

def abrir_navegador():
    wb.open('https://www.youtube.com/results?search_query=cuarteto+de+nos')

# escuchar el audio con el micro del pc
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Dime!")
    say_sabina("Dime!")
    audio = r.listen(source)

try:
    # si se entendió el audio
    comando = r.recognize_google(audio, language="es-MX")
    # lo que se debe hacer con el comando de audio
    interpretar(comando)
except sr.UnknownValueError:
    # si no entendió
    print("No te pude entender")
except sr.RequestError as e:
    # si no tiene conexión a internet o al servicio de google
    print(f'No pude obtener respuesta del servicio de reconocimiento de voz {e}')