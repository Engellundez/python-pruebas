from tkinter import Tk
from src.product import Product

def main():
    window = Tk()
    application = Product(window)
    window.mainloop()


if __name__ == '__main__':
    main()
