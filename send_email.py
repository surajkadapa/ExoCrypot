#sending email page
from tkinter import *
send_addr= ""
def get_addr():
    global send_addr
    send_addr = to_addr.get("1.0", "end-1c")
    


root = Tk()
root.title("ExoCrypt-Send Email")
root.geometry('950x700')
root.resizable(False, False)
root ['bg'] = "#322C2C"
back_button = Button(root, text="Back", command=root.destroy)
back_button.place(x=0, y=0)
comic=("Comic Sans MS",32,"bold")
head=Label(root,bg='#322c2c',fg='#ffffff',text='ExoCrypt',font=comic)
head.configure(justify='center')
head.place(x=395, y=20)
comic1=("Ubuntu",15,"bold")
title = Label(root, bg="#322c2c",fg="#ffffff", text="Send Email", font=comic1)
title.configure(justify='center')
title.place(x=420, y=76)
to_card = Label(root, text="To:", font=21)
to_card.place(x=90,y=150)
to_addr = Text(root, height=1, width=50)
to_addr.place(x=160,y=149)
attachment = Button(root, text="Attach files") #add attachement function
attachment.place(x=650,y=145)
body_card = Label(root, text="Body:", font=21)
body_card.place(x=90, y=193)
body = Text(root, height=20, width=80)
body.place(x=160, y=190)
submit = Button(root, text="Submit") #add submit function
submit.place(x=685, y=550)


root.mainloop()