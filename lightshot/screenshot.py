# Tomar screenshot con python
import pyautogui
import time

screanshot = pyautogui.screenshot()
screanshot.save(r"C:\\Users\\Engel Lundez\\OneDrive\\Imágenes\\Capturas de pantalla\\screenshot{0}.png".format(time.time))