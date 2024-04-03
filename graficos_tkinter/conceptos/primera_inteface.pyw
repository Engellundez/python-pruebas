from tkinter import *
# raíz es la convención para la variable de la clase Tk
ventana = Tk()

ventana.title("Ventana de pruebas")

# impedir la re-dimensión de la ventana a lo alto y ancho resizable(width, height)
# ventana.resizable(False, True)

# mostrar un icono personalizado en lugar del predefinido
ventana.iconbitmap("icon.ico")

# re-dimensionamos el tamaño base de la ventana
ventana.geometry("650x350")

ventana.config(background="blue")

# el mainloop es lo que ejecuta la ventana de manera indefinida hasta que esta se cierre
ventana.mainloop()
