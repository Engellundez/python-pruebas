from tkinter import Label, Button, Entry, Frame, messagebox, Text, Scrollbar, Radiobutton, IntVar
from tkinter.ttk import Combobox
from libFracMix import FracMix


class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.var_op = IntVar()
        self.master = master
        self.pack(expand=True, fill='both')
        self.create_widgets()

    def fnCalcular(self):
        try:
            e1 = int(self.text1E.get())
            n1 = int(self.text1N.get())
            d1 = int(self.text1D.get())
            f1 = FracMix(e1, n1, d1)

            e2 = int(self.text2E.get())
            n2 = int(self.text2N.get())
            d2 = int(self.text2D.get())
            f2 = FracMix(e2, n2, d2)
            
            # Combobox
            # index = self.cmbOpciones.current()
            # radioButtons
            index = self.var_op.get()
            
            if index == 0:
                f3 = f1 + f2
            elif index == 1:
                f3 = f1 - f2
            elif index == 2:
                f3 = f1 * f2
            elif index == 3:
                f3 = f1 / f2
            elif index == 4:
                f3 = ''
                if f1 == f2:
                    opt = 'son iguales'
                else:
                    opt = 'no son iguales'
                
                messagebox.showinfo(title='Fracciones Mixtas', message=f'Las opciones {opt}')
        except ValueError:
            f3 = 'Valor Inesperado'

        # LABEL
        # self.txtRes['text'] = f3
        # ENTRY
        # self.txtRes.delete(0, 'end')
        # self.txtRes.insert(0, f3)
        # TEXT
        # self.txtRes.delete(1.0, 'end')
        self.txtRes.insert(1.0, f'{f3}\n')

    def create_widgets(self):
        self.text1E, self.text1N, self.text1D = self.__widget_frame_fracmix__(30,30)
        self.text2E, self.text2N, self.text2D = self.__widget_frame_fracmix__(180,30)

        Label(self, text="Fracción 1: ").place(x=48, y=8)
        Label(self, text="Fracción 2: ").place(x=198, y=8)

        Label(self, text="Resultado: ").place(x=30, y=90)
        Label(self, text="Operación: ").place(x=30, y=150)

        p_aux = Frame(self)
        p_aux.place(x=100, y=90)
        
        scroll = Scrollbar(p_aux)
        scroll.pack(side='right', fill='y')
        
        # self.txtRes = Label(self, width=15, text='esperando ...')
        # self.txtRes = Entry(self, width=15)
        # Debe existir el scroll para poder invocar el yscrollcommand
        self.txtRes = Text(p_aux, width=12, height=3, yscrollcommand=scroll.set)
        
        self.txtRes.pack(side='left')
        # sirve para bajar y subir con el scroll de la caja de texto de txtRes
        scroll.config(command=self.txtRes.yview)

        self.btnCalcular = Button(self, text="Calcular", command=self.fnCalcular)
        self.btnCalcular.place(x=210, y=150)
        
        # COMBOBOX
        
        # los messageBox tienen diferentes propiedades que podemos utilizar, estas siempre tendrán un Titulo, un mensaje y 
        # un icono a utilizar, messagebox.showinfo(), messagebox.showwarning(), messagebox.showerror() a de más también podemos 
        # agregar o utilizar los messagebox de Interrogación y regresan (True/False) y son: 
        # messagebox.askyesno(), messagebox.askokcancel(), messagebox.askretrycancel(), messagebox.askquestion()
        # messagebox.askyesnocancel() Este devuelve (True, False, None)
        # opciones = ["Suma", "Resta", "Multiplicación", "División", "¿Son Iguales?"]
        # state: (readonly, disabled, None)
        # cmbOpciones.current(0) selecciona una opción desde el código
        # cmbOpciones.get() Obtiene el elemento seleccionado
        # cmbOpciones.current() Obtiene el indice del elemento seleccionado
        # self.cmbOpciones = Combobox(self, width=10, values=opciones, state='readonly')
        # self.cmbOpciones.place(x=100, y=150)
        # self.cmbOpciones.current(0)
        
        # RADIOBUTTON
        
        r1 = Radiobutton(self, text="Suma", value=0, variable=self.var_op)
        r1.place(x=100,y=150)
        r2 = Radiobutton(self, text="Resta", value=1, variable=self.var_op)
        r2.place(x=100,y=180)
        r3 = Radiobutton(self, text="Multiplicación", value=2, variable=self.var_op)
        r3.place(x=100,y=210)
        r4 = Radiobutton(self, text="División", value=3, variable=self.var_op)
        r4.place(x=100,y=240)
    
    def __widget_frame_fracmix__(self, placeX, placeY):
        f_frac_1 = Frame(self, width=100, height=60)
        f_frac_1.place(x=placeX, y=placeY)
        fx1 = Frame(f_frac_1, height=27, width=42)
        fx1.grid(row=0, column=0, rowspan=2)
        
        Label(fx1, text="Ent").pack(side="left")
        Label(f_frac_1, text="Num").grid(row=0, column=2)
        Label(f_frac_1, text="Den").grid(row=1, column=2)
        E = Entry(fx1, width=4)
        N = Entry(f_frac_1, width=4)
        D = Entry(f_frac_1, width=4)
        # Al usar Entry, el posicionamiento debe ser posterior a la creación ya que si se crea el elemento y se posiciona 
        # como lo hace Label, después no podremos acceder a las diferentes propiedades extras 
        E.pack(side="right")
        N.grid(row=0, column=1)
        D.grid(row=1, column=1)
        
        return (E,N,D)
