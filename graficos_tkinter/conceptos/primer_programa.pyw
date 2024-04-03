from tkinter import Tk, Label, Button

def mensaje():
    print("Mensaje del botón ")
    
def main():
    ventana = Tk()
    ventana.geometry("400x280")
    ventana.title("Ventana Hola Mundo")
    
    lbl = Label(ventana, text="Este es un [Label] tkinter")
    lbl.config(fg="green")
    lbl["bg"] = "gray"
    # Pack, ubica los widgets en una posición que podemos cambiar con los tributos adecuados
    lbl.pack()
    
    btn = Button(ventana, text="Presiona este [Button] para mensaje", bg="yellow", fg="blue", command=mensaje)
    btn.pack()
    
    ventana.mainloop()
    
main()