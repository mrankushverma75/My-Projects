import smtplib
import os
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('500x500')
root.title("Mail Sender")
root.resizable(0,0)
root.configure(background = "black")

x = StringVar()
y = StringVar()
z = StringVar()
q = StringVar()

lab1 = Label(root, text = "** Mail Sender **", font = ("Allura",30), fg = "white", bg = "black")
lab1.pack()
lab2 = Label(root, text = "Sender Email", font = ("Times New Roman",20), fg = "white", bg = "black")
lab2.pack(pady = 10)
ent = Entry(root, font = ("Times New Roman",10),width = 25, fg = "black", bg = "white", textvariable = x)
ent.pack(pady = 5, ipady = 5, ipadx = 10)

ent3 = Entry(root, show = "*", width = 25, font = ("Times New Roman",10),textvariable = q)
ent3.pack(pady = 5, ipady = 5, ipadx = 10)

lab3 = Label(root, text = "Recipient Email", font = ("Times New Roman",20), fg = "white", bg = "black")
lab3.pack(pady = 10)
ent1 = Entry(root, font = ("Times New Roman",10),width = 25, fg = "black", bg = "white", textvariable = y)
ent1.pack(pady = 5, ipady = 5, ipadx = 10)

lab4 = Label(root, text = "Enter Message", font = ("Times New Roman",20), fg = "white", bg = "black")
lab4.pack(pady = 10)
ent2 = Entry(root, font = ("Times New Roman",10),width = 25, fg = "black", bg = "white", textvariable = z)
ent2.pack(pady = 5, ipady = 5, ipadx = 10)



def send_fun():
    sender = x.get()
    passwd = q.get()
    sec_id = y.get()
    msg_id = z.get()
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.starttls()
    mail.login(sender,passwd)
    sender = sender
    recipient = sec_id
    content = msg_id
    mail.sendmail(sender,recipient,content)
    print("sent")


send_btn = Button(root, text = "Send", compound = "left", width = 10, command = send_fun,border = 0)
send_btn.pack(padx = 10, side = "left")

multi_btn = Button(root,text = "Multi Line Msg", compound = "left", width = 10, command = send_fun,border = 0)
multi_btn.pack(padx = 10, side = "left")

bulk_btn = Button(root,text = "Bulk Msg", compound = "left", width = 10, command = send_fun,border = 0)
bulk_btn.pack(padx = 10, side = "left")

attach_btn = Button(root,text = "Attach", compound = "left", width = 10, command = send_fun,border = 0)
attach_btn.pack(padx = 10, side = "left")

root.mainloop()