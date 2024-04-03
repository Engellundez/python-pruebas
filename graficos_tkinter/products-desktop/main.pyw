from tkinter import ttk
from tkinter import *
import sqlite3


class Product(Frame):
    def __init__(self, window) -> None:
        self.wind = window
        self.wind.title('Products Application')


def main():
    window = Tk()
    application = Product(window)
    window.mainloop()


if __name__ == '__main__':
    main()
