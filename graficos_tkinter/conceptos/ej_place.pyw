from tkinter import Tk, Label, Button, Entry

def main():
    vent = Tk()
    vent.title("EJ Place")
    vent.geometry("400x200")
    
    def sumar():
        result.delete(0, 'end')
        try:
            n1 = float(num1.get())
            n2 = float(num2.get())
            r = n1+n2
            result.insert(0, r)
        except:
            result.insert(0, 'No son números')

    lbl1 = Label(vent, text="Primer Número", bg="yellow")
    # lbl1.place(x=10,y=10, height=30, width=100)
    lbl1.place(relx=0.03,rely=0.03, relheight=0.1, relwidth=0.22)
    
    num1 = Entry(vent, bg="pink")
    # num1.place(x=120,y=10, height=30, width=100)
    num1.place(relx=0.28,rely=0.03, relheight=0.1, relwidth=0.22)

    lbl2 = Label(vent, text="Segundo Número", bg="yellow")
    # lbl2.place(x=10,y=50, height=30, width=100)
    lbl2.place(relx=0.03,rely=0.15, relheight=0.1, relwidth=0.22)
    
    num2 = Entry(vent, bg="pink")
    # num2.place(x=120,y=50, height=30, width=100)
    num2.place(relx=0.28,rely=0.15, relheight=0.1, relwidth=0.22)
    
    btn = Button(vent, text="Sumar", command=sumar)
    # btn.place(x=230, y=50, height=30, width=80)
    btn.place(relx=0.55, rely=0.15, relheight=0.1, relwidth=0.22)

    lbl3 = Label(vent, text="Resultado", bg="yellow")
    # lbl3.place(x=10,y=90, height=30, width=100)
    lbl3.place(relx=0.03,rely=0.27, relheight=0.1, relwidth=0.22)

    result = Entry(vent, bg="pink")
    # result.place(x=120,y=90, height=30, width=100)
    result.place(relx=0.28,rely=0.27, relheight=0.1, relwidth=0.22)

    vent.mainloop()
    
main()