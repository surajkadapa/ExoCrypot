import tkinter as tk
from tkinter import * 
import base64
m = Tk()
#322c2c

m.title('ExoCrypt')
m.geometry('950x700')
m['bg']='#322c2c'
m.resizable(False,False)
name = ""
password = ""
fl = open("/home/suraj/Documents/personal/ExoCrypot/credentials.txt") #the path problem should be taken care of
cred = fl.read().split()
user = cred[0]
pasw = cred[1]

#login page

def login():
    global m
    global user, pasw
    print(user,pasw)
    m.destroy()
    def my_show():
        #print(c_v1.get())
        if(c_v1.get()==1):
            passw_entry.config(show='')
        else:
            passw_entry.config(show='*')


    def submit():
        global name, password
        name = name_var.get()
        password = passw_var.get()
        #print(name, password)
        credentials(name, password)

    def credentials(guser, gpass):
        global user, pasw
        #print(guser, gpass)
        if user == guser and gpass == pasw:
            msg.insert(END, "Success!")
        else:
            msg.insert(END, "Recheck username and password!")

    root = tk.Tk()
    root.title("ExoCrypt-Login")
    root.geometry('950x700')
    root.resizable(False, False)
    root ['bg'] = '#322C2C'
    Font_tuple = ("Comic Sans MS", 25, "bold")
    Font_tuple2 = ("Ubuntu", 18)
    heading = tk.Label(root, bg="#322C2C", fg="#ffffff", text= "ExoCrypt", font=Font_tuple)
    heading.configure(justify="center")
    heading.place(x=400, y=10)
    heading2 = tk.Label(root, bg="#322C2C", fg="#ffffff", text="Login", font=Font_tuple2)
    heading2.configure(justify=CENTER)
    heading2.place(x=435, y=50)
    name_var = tk.StringVar(root)
    passw_var = tk.StringVar(root)
    name_disp = tk.Label(root, text='Username', bg="#322C2C", fg="#ffffff")
    name_disp.place(x=365, y=300)
    name_entry = tk.Entry(root, textvariable=name_var)
    name_entry.place(x=445, y=298)
    passw_entry = tk.Entry(root, show ="*", textvariable=passw_var)
    passw_disp = tk.Label(root, text="Password", bg='#322C2C', fg="#ffffff")
    passw_disp.place(x=366, y=340)
    passw_entry.place(x=445, y=338)
    c_v1=IntVar(root)
    c1 = Checkbutton(root,text='Show Password',variable=c_v1,onvalue=1,offvalue=0,command=my_show)
    c1.place(x=457, y=370)
    msg = tk.Text(root, height=1, width=50,bg="#322C2C",fg="#ffffff")
    msg.place(x=300, y=440)
    sub_btn = tk.Button(root, text="Submit", command=submit)
    sub_btn.place(x=460, y=400)
    back_button = tk.Button(root, text="Back", command=root.destroy)
    back_button.place(x=0,y=0)
    root.mainloop()
    print(name, password)

#Decrypt Page

def decry():
    def get_txt():
        INPUT = enc_text.get("1.0", "end-1c")
        return decrypt(INPUT)

    def insert_txt():
        dec_text.insert(END, get_txt())

    def decrypt(text):
        return (base64.b64decode(text).decode('utf-8'))

    m2 = tk.Tk()
    m2.title("ExoCrypt")
    m2.geometry('950x700')
    m2.resizable(False,False)
    m2 ['bg'] = "#322C2C"
    Font_tuple = ("Comic Sans MS", 25, "bold")
    Font_tuple2 = ("Ubuntu",18)
    heading = tk.Label(m2, bg="#322C2C", fg="#ffffff", text= "ExoCrypt", font=Font_tuple)
    heading.configure(justify="center")
    heading.place(x=400, y=20)
    back_button = tk.Button(m2, text="Back", command=m2.destroy)
    back_button.place(x=30,y=20)
    enc_lbl=tk.Label(m2, bg="#322C2C", fg = "#ffffff", text="Encrypted Text", font=Font_tuple2)
    enc_lbl.place(x=142,y=116)
    dec_lbl=tk.Label(m2, bg="#322C2C", fg = "#ffffff", text="Decrypted Text", font=Font_tuple2)
    dec_lbl.place(x=622,y=116)
    enc_text = tk.Text(m2, height=20, width=50)
    enc_text.place(x=30, y=150)
    dec_text = tk.Text(m2, height=20, width=50)
    dec_text.place(x=500, y=150)
    dec_button = tk.Button(m2, text="Decrypt", height = 2, width = 12, command=insert_txt)
    dec_button.place(x=410,y=550)
    m2.mainloop()

#Exocrypt heading
comic=("Comic Sans MS",32,"bold")
head=tk.Label(m,bg='#322c2c',fg='#ffffff',text='ExoCrypt',font=comic)
head.place(x=395, y=175)
head.configure(justify='center')

#logo
logo = PhotoImage(file="/home/suraj/Documents/personal/ExoCrypot/exo_1.png")
Label(image=logo,bg="#322C2C").place(x=385, y=230)

#Send Button
send=tk.Button(m,text='Send', width = 40, command=login)
send.place(x=80,y=430)

#Decrypt Button
decry=tk.Button(m,text='Decrypt', width = 40, command=decry)
decry.place(x=505,y=430)

m.mainloop()
