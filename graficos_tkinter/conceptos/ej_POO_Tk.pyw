from tkinter import Tk, Frame, Button

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.hi_there = Button(self)
        self.hi_there['text'] = "Hello World\n (Click Me)"
        self.hi_there['command'] = self.say_hi
        self.hi_there.pack(side='top')
        
        # master.destroy cierra la ventana principal
        self.quit = Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side='bottom')
    
    def say_hi(self):
        print("hi there, everyone")

def main():
    root = Tk()
    app = Application(root)
    app.mainloop()

if __name__ == '__main__':
    main()