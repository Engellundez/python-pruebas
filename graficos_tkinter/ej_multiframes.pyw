from tkinter import Button, Frame, Tk

root = Tk()
root.title("Frames")
root.geometry("200x70")

frame_1 = Frame(root, bg="blue")
frame_1.pack(expand=True, fill='both')

frame_2 = Frame(root, bg='yellow')
frame_2.pack(expand=True, fill='both')
# cambiamos el cursor cuando se encuentre en este frame_2.
frame_2.config(cursor='heart')

red_btn = Button(frame_1, text='Red', fg='red')
green_btn = Button(frame_1, text='Green', fg='green')
blue_btn = Button(frame_1, text='Blue', fg='blue')

red_btn.place(relx=.05, rely=.05,relwidth=.25,relheight=.9)
green_btn.place(relx=.35, rely=.05,relwidth=.25,relheight=.9)
blue_btn.place(relx=.65, rely=.05,relwidth=.25,relheight=.9)

black_btn = Button(frame_2, text='Black', fg="black")
black_btn.pack()

root.mainloop()