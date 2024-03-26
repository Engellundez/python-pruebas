# Tomar screenshot con python
import pyautogui
from datetime import datetime

now = datetime.now()
default_dir = r"C:\\Users\\Engel Lundez\\OneDrive\\Imágenes\\Capturas de pantalla\\"

this_dir = r"C:\\inetpub\\wwwroot\\python\\soyDaltoPython\\lightshot\\"

image_dir = r"C:\\Users\\Engel Lundez\\OneDrive\\Imágenes\\"

default_name = "screenshot{0}.PNG".format(now.strftime('%d_%m_%Y_%H_%M'))

file_name = f"{this_dir}{default_name}"
# file_name = f"{image_dir}clac.jpg"
print(file_name)
# get screenshot
screenshot = pyautogui.screenshot(file_name)
screenshot.save()

# screenshot_to_edit = pyautogui.locateOnScreen(file_name)
