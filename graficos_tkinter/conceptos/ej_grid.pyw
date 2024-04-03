from tkinter import Tk, Button, Entry, Label

def main():
    vent = Tk()
    # vent.geometry("600x450")
    vent.title("Grid")
    vent.config(padx=20, pady=20)
    
    vent.columnconfigure(0, weight=1)
    vent.columnconfigure(1, weight=1)
    vent.rowconfigure(2, weight=1)
    
    entry = Entry(vent)
    entry.grid(row=0, column=0, rowspan=2, sticky='we')
    
    btn = Button(vent, text="Presione aquí")
    btn.grid(row=0, column=2, rowspan=2)
    
    lbl = Label(vent, text='Hola, Mundo!')
    lbl.grid(row=2, column=0, columnspan=3, sticky='wnse')
    
    vent.mainloop()
    
main()