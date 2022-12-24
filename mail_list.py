#page to display inbox
import smtplib, time, imaplib, email
from email import policy
import traceback, mailparser
from bs4 import BeautifulSoup
from tkinter import *
frm_email = "testpython333@gmail.com"
frm_pwd = "wkpltoxkaklffbpm"
smtp_server = "imap.gmail.com"
smtp_port = 993
msg = ""
arr = []
mail = imaplib.IMAP4_SSL(smtp_server)
mail.login(frm_email,frm_pwd)
mail.select('inbox')
data = mail.search(None, 'ALL')
mail_ids = data[1]
id_list = mail_ids[0].split()   
first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])
print(first_email_id,latest_email_id)

l = None

def get_email(n):
    global msg, arr
    try:
        for i in range(2,first_email_id, -1):
            data = mail.fetch(str(n), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_bytes(arr[1], policy=policy.default)
    except Exception as e:
        traceback.print_exc() 
        print(str(e))

def get_deets():
    mail = mailparser.parse_from_bytes(arr[1])
    frm = msg['from']
    date = mail.date
    sub = mail.subject
    soup = BeautifulSoup(' '.join(map(str, mail.text_html)), 'html.parser')
    body = soup.get_text()
    return (frm, date, sub, body)

get_email(6453)
frm, date, sub, body = get_deets()
print(frm, date, sub, body)
print("*************************************************************")

get_email(6454)
frm, date, sub, body = get_deets()
print(frm, str(date), sub, body)


####################################################################################################################
root = Tk()
root.title("ExoCrypt-Inbox")
root.geometry('950x700')
root.resizable(False, False)
root ['bg'] = "#322C2C"
back_button = Button(root, text="Back", command=root.destroy)
back_button.place(x=0,y=0)
Button(text=frm+str(date)+sub+body).place(x=10, y=10)
root.mainloop()