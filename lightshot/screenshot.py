# Tomar screenshot con python
import pyautogui
import time

print(time.time())
screanshot = pyautogui.screenshot()
screanshot.save(r"C:\\Users\\Engel Lundez\\OneDrive\\Imágenes\\Capturas de pantalla\\screenshot.png")