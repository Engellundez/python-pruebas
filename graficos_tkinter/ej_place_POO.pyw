from tkinter import Tk, Label, Button, Entry, Frame

class MyVentana(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=320, height=170)
        self.master = master
        self.pack()
        self.create_widgets()
        
        
    def sumar(self):
        self.result.delete(0, 'end')
        try:
            n1 = float(self.num1.get())
            n2 = float(self.num2.get())
            r = n1+n2
            self.result.insert(0, r)
        except:
            self.result.insert(0, 'No son números')

    def create_widgets(self):
        self.lbl1 = Label(self, text="Primer Número", bg="yellow")
        self.num1 = Entry(self, bg="pink")
        self.lbl2 = Label(self, text="Segundo Número", bg="yellow")
        self.num2 = Entry(self, bg="pink")
        self.btn = Button(self, text="Sumar", command=self.sumar)
        self.lbl3 = Label(self, text="Resultado", bg="cyan")
        self.result = Entry(self, bg="cyan")

        self.lbl1.place(x=10, y=10, height=30, width=100)
        self.num1.place(x=120, y=10, height=30, width=100)
        self.lbl2.place(x=10, y=50, height=30, width=100)
        self.num2.place(x=120, y=50, height=30, width=100)
        self.btn.place(x=230, y=50, height=30, width=80)
        self.lbl3.place(x=10, y=90, height=30, width=100)
        self.result.place(x=120, y=90, height=30, width=100)


def main():
    vent = Tk()
    vent.title("EJ Place")
    # vent.wm_title("EJ Place")
    app = MyVentana(vent)
    frame2 = Frame(vent, bg='yellow', width=80, height=30)
    frame2.pack()

    app.mainloop()


main()
