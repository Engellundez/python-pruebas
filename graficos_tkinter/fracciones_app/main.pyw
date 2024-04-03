from tkinter import Tk
from mainFrame import MainFrame


def main():
    ventana = Tk()
    ventana.title('Fracciones Mixtas')
    ventana.geometry('320x350')
    app = MainFrame(ventana)
    app.mainloop()


if __name__ == '__main__':
    main()
