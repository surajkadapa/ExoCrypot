#decrypt page
from tkinter import *
import base64

def get_txt():
    INPUT = enc_text.get("1.0", "end-1c")
    return decrypt(INPUT)

def insert_txt():
    dec_text.insert(END, get_txt())

def decrypt(text):
    return (base64.b64decode(text).decode('utf-8'))


root = Tk()
root.title("ExoCrypt-Decrypt")
root.geometry('950x700')
root.resizable(False,False)
root ['bg'] = "#322C2C"
Font_tuple = ("Comic Sans MS", 25, "bold")
Font_tuple2 = ("Ubuntu", 18)
heading = Label(root, bg="#322C2C", fg="#ffffff", text= "ExoCrypt", font=Font_tuple)
heading.configure(justify="center")
heading.place(x=400, y=10)
back_button = Button(root, text="Back", command=root.destroy)
back_button.place(x=0,y=0)
enc_lbl = Label(root, bg="#322C2C", fg = "#ffffff", text="Encrypted Text", font=Font_tuple2)
enc_lbl.place(x=142,y=116)
dec_lbl = Label(root, bg="#322C2C", fg = "#ffffff", text="Decrypted Text", font=Font_tuple2)
dec_lbl.place(x=622,y=116)
enc_text = Text(root, height=20, width=50)
enc_text.place(x=30, y=150)
dec_text = Text(root, height=20, width=50)
dec_text.place(x=500, y=150)
dec_button = Button(root, text="Decrypt", height = 2, width = 12, command=insert_txt)
dec_button.place(x=410,y=550)
root.mainloop()