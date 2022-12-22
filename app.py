from tkinter import *
#from tkinter.ttk import *
root = Tk()

root.title("ExoCrypt")
root.geometry('950x700')
root ['bg'] ='#322C2C'
Font_tuple = ("Comic Sans MS", 32, "bold")
heading = Label(root,  bg="#322C2C", fg="#ffffff", text = "ExoCrypt", font=Font_tuple)
heading.configure(justify='center')
heading.place(x=385,y=10)
root.resizable(False,False)
photo = PhotoImage(file=r"/home/suraj/Documents/random/gui")

root.mainloop()