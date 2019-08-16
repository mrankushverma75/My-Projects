from tkinter import *
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

root = Tk()
root.title("Whatsapp Bomber :: Develope By : Ankush Verma")
root.geometry('500x500')
root.resizable(0,0)
root.config(bg = "#a0d44c")

x = StringVar()
y = IntVar()
z = StringVar()

def send_fun():

     name = x.get()
     msg = z.get()
     count = y.get()

     user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
     user.click()

     msg_box = driver.find_element_by_class_name('_13mgZ')

     for i in range(count):
         msg_box.send_keys(msg)
         button = driver.find_element_by_class_name('_3M-N-')
         button.click()

     x.set("")
     y.set("")
     z.set("")

     prompt = Toplevel(root)
     prompt.title("Delivery Status")
     prompt.geometry('200x80+250+250')
     prompt.resizable(0,0)
     prompt.config(bg = "#fac525")

     status = Label(prompt,image = success_img,text="  Successfully Sent",font =("Gabriola",20),bg ="#fac525",compound = "left")
     status.pack(pady = 10)
     prompt.mainloop()


whatsapp_img = PhotoImage(file = 'whatsapp.png')
team_img = PhotoImage(file = 'teamwork.png')
bunch_img = PhotoImage(file = 'raspberry.png')
send_img = PhotoImage(file = 'send.png')
msg_img = PhotoImage(file = 'love.png')
success_img = PhotoImage(file = 'success.png')

lab = Label(root, image = whatsapp_img, bg = "#a0d44c")
lab.pack(pady = 5)

name_lbl = Label(root, text = "  Enter the Person or Grp Name" ,image = team_img , compound = "left", font = ("Gabriola",20), bg = "#a0d44c")
name_lbl.pack()
user_name = Entry(root, text = "", bg = "#45d9d1", width = 20, font = ("Arial", 15), textvariable = x)
# user_name.insert(0, "Enter Name")
user_name.pack(pady = 10, ipadx = 2, ipady = 2)


msg_lbl = Label(root, text = "   Enter the Message" ,image = msg_img, compound = "left", font = ("Gabriola",20), bg = "#a0d44c")
msg_lbl.pack()
usr_msg = Entry(root, text = "", bg = "#45d9d1", width = 20, font = ("Arial", 15), textvariable = z)
usr_msg.pack(pady = 10, ipadx = 2, ipady = 2)

no_msgs_lbl = Label(root, text = "   Enter the No. of Messages" ,image = bunch_img, compound = "left", font = ("Gabriola",20), bg = "#a0d44c")
no_msgs_lbl.pack()
bunch_msg = Entry(root, text = "", bg = "#45d9d1", width = 5, font = ("Arial", 15), textvariable = y)
bunch_msg.pack(pady = 10, ipadx = 2, ipady = 2)

send_btn = Button(root, text = "  Send", font = ("Gabriola",20), image = send_img, compound = "left", bd = 0, bg = "#a0d44c",
                  command = send_fun)
send_btn.pack(pady = 5)

root.mainloop()
