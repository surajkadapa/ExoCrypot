#login page
from tkinter import *
name = ""
password = ""
fl = open("/home/suraj/Documents/personal/ExoCrypot/credentials.txt")
cred = fl.read().split()
user = cred[0]
pasw = cred[1]

def submit():
    global name, password
    name = name_var.get()
    password = passw_var.get()
    credentials(name, password)

def credentials(guser, gpass):
    global user, pasw
    if user == guser and gpass == pasw:
        msg.insert(END, "Success!")
    else:
        msg.insert(END, "Recheck username and password!")

root = Tk()
root.title("ExoCrypt-Login")
root.geometry('950x700')
root.resizable(False, False)
root ['bg'] = '#322C2C'
Font_tuple = ("Comic Sans MS", 25, "bold")
Font_tuple2 = ("Ubuntu", 18)
heading = Label(root, bg="#322C2C", fg="#ffffff", text= "ExoCrypt", font=Font_tuple)
heading.configure(justify="center")
heading.place(x=400, y=10)
heading2 = Label(root, bg="#322C2C", fg="#ffffff", text="Login", font=Font_tuple2)
heading2.configure(justify=CENTER)
heading2.place(x=435, y=50)
name_var = StringVar()
passw_var = StringVar()
name_disp = Label(root, text='Username', bg="#322C2C", fg="#ffffff")
name_disp.place(x=365, y=300)
name_entry = Entry(root, textvariable=name_var)
name_entry.place(x=445, y=298)
passw_entry = Entry(root, show ="*", textvariable=passw_var)
passw_disp = Label(root, text="Password", bg='#322C2C', fg="#ffffff")
passw_disp.place(x=366, y=340)
passw_entry.place(x=445, y=338)
msg = Text(root, height=1, width=50,bg="#322C2C",fg="#ffffff")
msg.place(x=300, y=420)
sub_btn = Button(root, text="Submit", command=submit)
sub_btn.place(x=460, y=380)
back_button = Button(root, text="Back", command=root.destroy)
back_button.place(x=0,y=0)
root.mainloop()
print(name, password)