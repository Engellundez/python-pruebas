from tkinter import Tk, Button, Entry

def main():
    vent = Tk()
    vent.geometry("600x450")
    vent.title("Pack")
    vent.config(padx=20, pady=20)
    
    entry = Entry(vent)
    entry.pack()
    
    btn = Button(vent, text="Hola, Mundo!")
    btn.pack(side="left", expand=True, fill="y", before=entry)
    
    vent.mainloop()
    
main()