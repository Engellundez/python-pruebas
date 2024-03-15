import speech_recognition as sr
import subprocess as sub
import pyautogui as auto
import pyttsx3 as voz
from time import sleep

def interpretar(comando_de_audio):
    comando_de_audio = comando_de_audio.split(' ')
    ver_video = ('vídeo' or 'video') in comando_de_audio
    escribir = ('escribir' or 'texto') in comando_de_audio
    
    if ver_video is True:
        abrir_youtube()
    elif escribir is True:
        abrir_blocNotas()
        
def abrir_blocNotas():
    sub.call('start notepad.exe', shell=True)
    sleep(1)
    texto = 'Estoy listo para escribir tu texto'
    auto.write(texto)
    sabina = voz.init()
    velocidad = sabina.getProperty('rate')
    sabina.setProperty('rate', velocidad-25)
    sabina.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
    sabina.say(texto)
    sabina.runAndWait()
    pass

def abrir_youtube():
    sub.call(r'[direccion al archivo batch]/navegar.bat')
    pass