import pyautogui
# from PIL import Image

# Tomar una captura de pantalla
screenshot = pyautogui.screenshot()

# Supongamos que queremos recortar la imagen: define las coordenadas del recorte
# (izquierda, arriba, derecha, abajo)
box = (800, 800, 1500, 1500)

# Realizar el recorte usando Pillow
edited_image = screenshot.crop(box)

# Mostrar la imagen editada
edited_image.show()

# Guardar la imagen editada, si se desea
edited_image.save('edited_screenshot.png')
