import speech_recognition as sr
import webbrowser as wb

def fn_speech_recognition():
    sr.Microphone(device_index=0)
    # Creating a recognition object
    r = sr.Recognizer()
    # Sound Quality
    r.energy_threshold=400
    # Para la sensibilidad
    r.dynamic_energy_threshold = False
    
    with sr.Microphone() as source:
        print('Please Speak Loud and Clear: ')
        # reduce noise
        r.adjust_for_ambient_noise(source)
        # take voice input from the microphone
        audio = r.listen(source)
        
        try:
            phrase = r.recognize_google(audio, language="es-MX")
            print(f'Did you just say: {phrase}')
            url = "https://www.google.com/search?q="
            search_url = url+phrase
            wb.open(search_url)
        # except TimeoutException as msg:
        except sr.UnknownValueError as msg:
            print("I don't how are you say")
        except TimeoutError as msg:
            print(msg)
        except sr.WaitTimeoutError:
            print("listening timed out while waiting for phrase to start")
        except LookupError:
            print("Could not understand what you've requested.")
        else:
            print("Your results will appear in the default browser. Good bye for now...")
            
fn_speech_recognition()