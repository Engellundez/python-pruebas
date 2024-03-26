import tkinter as tk
from tkinter import Toplevel, Canvas
import pyautogui
from PIL import ImageGrab
import time

class ScreenCaptureTool:
    def __init__(self, root):
        self.root = root
        self.sx = self.sy = self.ex = self.ey = 0
        self.rect = None

        self.top = Toplevel(root)
        self.top.overrideredirect(1)  # Sin bordes
        self.top.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        self.top.wait_visibility(self.top)
        self.top.wm_attributes('-alpha',0.4)  # Semi-transparencia

        self.c = Canvas(self.top, cursor="cross", bg="grey11")
        self.c.pack(fill="both", expand=True)

        self.c.bind("<ButtonPress-1>", self.on_button_press)
        self.c.bind("<B1-Motion>", self.on_move_press)
        self.c.bind("<ButtonRelease-1>", self.on_button_release)

        self.top.mainloop()

    def on_button_press(self, event):
        # Inicio de la selección
        self.sx = self.c.canvasx(event.x)
        self.sy = self.c.canvasy(event.y)

        if not self.rect:
            self.rect = self.c.create_rectangle(self.sx, self.sy, self.sx, self.sy, outline='red')

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)
        
        # Actualizar el rectángulo según el mouse
        self.c.coords(self.rect, self.sx, self.sy, curX, curY)

    def on_button_release(self, event):
        self.ex = self.c.canvasx(event.x)
        self.ey = self.c.canvasy(event.y)

        # Finalizar la selección y capturar
        self.capture_selected_area()

        # Cerrar la ventana después de la captura
        self.top.destroy()
        
    def capture_selected_area(self):
        # Corregir coordenadas en caso de selección inversa
        x1, y1 = sorted([self.sx, self.ex])[0], sorted([self.sy, self.ey])[0]
        x2, y2 = sorted([self.sx, self.ex])[1], sorted([self.sy, self.ey])[1]
        
        
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))

        # Guardar o procesar la imagen
        img.save('capture.png')
        img.show()


root = tk.Tk()
root.withdraw()  # Esconder la ventana principal
app = ScreenCaptureTool(root)
