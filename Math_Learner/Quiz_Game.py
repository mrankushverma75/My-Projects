from tkinter import *
from PIL import Image, ImageTk
import random
import threading
import time as nt
from playsound import playsound
from matplotlib import pyplot as plt
root = Tk()
root.title("Math Learner  Develope By :: Ankush Verma")
root.geometry('500x500')
root.resizable(0, 0)
root.config(background="#deff9c")
chk_img = PhotoImage(file="D:\\Python\\Math_Learner\\completed-task.png")
sub_img = PhotoImage(file="D:\\Python\\Math_Learner\\right-arrow.png")
bitcoin_img = PhotoImage(file="D:\\Python\\Math_Learner\\bitcoin.png")
bitloss_img = PhotoImage(file="D:\\Python\\Math_Learner\\dollar.png")
bitup_img = PhotoImage(file="D:\\Python\\Math_Learner\\profit.png")
faq_img = PhotoImage(file="D:\\Python\\Math_Learner\\faq.png")
up_img = PhotoImage(file="D:\\Python\\Math_Learner\\up.png")
down_img = PhotoImage(file="D:\\Python\\Math_Learner\\down.png")
music = 'D:\Python\Math_Learner\water_drop.mp3'
drop_music = 'D:\Python\Math_Learner\drop.mp3'
wrong = 'D:\Python\Math_Learner\wrong.mp3'
wrong2 = 'D:\Python\Math_Learner\wrong2.mp3'
#img =Image.open("//root//Desktop//math_image.jpg")
# img.thumbnail((600,500))
# img1=ImageTk.PhotoImage(img)

x = DoubleVar()
lab = Label(root, text="Easy Math Learner", font=("Allura", 40),
            fg="red", bg="#c0ed66", borderwidth=3, relief="sunken")
lab.pack(ipadx=5, ipady=5, pady=5)
lab1 = Label(root, text="", font=(
    "Kaushan Script", 30), width=10, bg="#deff9c")
lab1.pack(pady=5)

ent = Entry(root, font=("Kaushan Script", 20),
            width=5, textvariable=x, bg="#f8fa6e")
ent.pack(pady=10, ipadx=5, ipady=2)


#op_choice = random.choice(operators)
# print(operators[op_choice])
xp_crt, xp_incrt, xp, pos_xp, neg_xp = 0, 0, 0, 0, 0
crt_res, in_crt_res, y_plot =[], [], []
count, count2 = 0, 0


def show():
    global j, count

    def sub_fun():
        # playsound(music)
        global xp_crt, xp_incrt, xp, crt_res, in_crt_res, pos_xp, neg_xp, count2, y_plot
        ent_val = x.get()
        x.set("0")
        crt_res.append(str(result))
        # print(result)
        if ent_val == result or ("%.2f" % ent_val) == result:
            # crt_res.append(str(result))
            playsound(music)
            in_crt_res.append("_")
            y_plot.append(10)
            xp += 10
            pos_xp += 10
            xp_crt += 1
            btn.destroy()
            # print("Answer is correct")
            chk_lab.config(text="Correct\n+10 XP", fg="green")

        else:
            playsound(wrong)
            in_crt_res.append(str(("%d" % ent_val)))
            # crt_res.append("_")
            y_plot.append(-5)
            xp -= 5
            neg_xp += 5
            xp_incrt += 1
            # print("Incorrect Answer")
            btn.destroy()
            chk_lab.config(text="Incorrect\n-5 XP", fg="red")
        count2 += 1
        return count2, y_plot
    if count <= 10:
        if count == 10:
            chk_lab.config(text="Round 1\nFinished")
        index = random.randrange(0, 3)
        operators = ["+", "-", "*", "/", "%"]
        num = random.randint(0, 20)
        num1 = random.randint(1, 10)

    elif count > 10 or count <= 20:
        if count == 20:
            chk_lab.config(text="Round 2\nStarted")
        index = random.randrange(0, 5)
        operators = ["+", "-", "*", "/", "%"]
        num = random.randint(0, 50)
        num1 = random.randint(1, 10)

    elif count > 20:
        if count == 21:
            chk_lab.config(text="Round 3\nStarted\nIt's Never End")
        index = random.randrange(0, 5)
        operators = ["+", "-", "*", "/", "%"]
        num = random.randint(0, 99)
        num1 = random.randint(1, 99)

    lab1.config(text=str(num)+" "+operators[index]+" "+str(num1), fg="#3308c2")

    if index == 0:
        result = num+num1
        # print(result)
    elif index == 1:
        result = num - num1
        # print(result)
    elif index == 2:
        result = num * num1
        # print(result)
    elif index == 3:
        y = num / num1
        result = ("%.2f" % y)
        # print(result)
    elif index == 4:
        result = num % num1
        # print(result)
    btn = Button(root, image=sub_img, text="Submit", font=("Arial Bold", 12),
                 compound="left", command=sub_fun, border=0, bg="#deff9c", fg="#cf0ab1")
    if count == count2:
        btn.pack(pady=10)

    time = threading.Timer(12.0, show)
    time.start()
    ent_val2 = ent.get()
    if ent_val2 == "" or count > count2:
        # nt.sleep(10)
        btn.destroy()
        time.cancel()
        chk_lab.destroy()
        chk_btn.pack(pady=5)
        playsound(wrong2)
        time_lbl = Label(root, text="Time Up \n Game Over", font=(
            "Kaushan Script", 30), width=10, fg="red",  bg="#deff9c")
        time_lbl.pack(pady=5)
    count += 1


def chk_fun():
    playsound(drop_music)
    root.withdraw()
    new_win = Toplevel()
    new_win.title("Math Learner  Develope By :: Ankush Verma")
    new_win.geometry('600x500')
    new_win.resizable(0, 0)
    new_win.config(background="#deff9c")
    total_xp = xp_crt + xp_incrt
    total = Label(new_win, text="Total Result", font=(
        "Kaushan Script", 20), width=10, bg="#deff9c", fg="#085aff")
    total.grid(row=0, column=0)
    crt_lbl = Label(new_win, text="Correct", font=(
        "Kaushan Script", 20), width=10, bg="#deff9c", fg="#085aff")
    crt_lbl.grid(row=0, column=1)
    incrt_lbl = Label(new_win, text="Incorrect", font=(
        "Kaushan Script", 20), width=10, bg="#deff9c", fg="#085aff")
    incrt_lbl.grid(row=0, column=2)
    xp_lbl = Label(new_win, text="  Ques : "+str(total_xp), font=("Kaushan Script", 15), image=faq_img,
                   compound="left", bg="#deff9c", fg="#ff3c00")
    xp_lbl.grid(row=1, column=0)
    xp_lbl1 = Label(new_win, text="  +XP : "+str(pos_xp), font=("Kaushan Script", 15), image=bitup_img,
                    compound="left", bg="#deff9c", fg="#ff3c00")
    xp_lbl1.grid(row=2, column=0)
    xp_lbl2 = Label(new_win, text="  -XP : "+str(neg_xp), font=("Kaushan Script", 15), image=bitloss_img,
                    compound="left", bg="#deff9c", fg="#ff3c00")
    xp_lbl2.grid(row=3, column=0)
    xp_lbl3 = Label(new_win, text=" Total XP : "+str(xp), font=("Kaushan Script", 15), image=bitcoin_img,
                    compound="left", bg="#deff9c", fg="#ff3c00")
    xp_lbl3.grid(row=4, column=0)

    for i in range(total_xp):
        xp_crt_lbl = Label(new_win, text=crt_res[i], font=(
            "Kaushan Script", 15), width=10, bg="#deff9c", fg="#ff3c00")
        xp_crt_lbl.grid(row=i+1, column=1)
        xp_incrt_lbl = Label(new_win, text=in_crt_res[i], font=(
            "Kaushan Script", 15), width=10, bg="#deff9c", fg="#ff0000")
        xp_incrt_lbl.grid(row=i+1, column=2)
    x_plot = []
    plt.title('Easy Math Learner')
    plt.xlabel('No. of Questions')
    plt.ylabel('Result')
    for i in range(total_xp):    
        x_plot.append(i)
    plt.scatter(x_plot, y_plot, color = 'g')
    plt.plot(x_plot, y_plot, color = 'r')
    plt.legend(['Result'])
    plt.show()
    new_win.mainloop()


chk_btn = Button(root, image=chk_img, text="Check Result", font=("Arial"),
                 compound="left", border=0, bg="#deff9c", fg="#cf0ab1", command=chk_fun)
chk_btn.pack_forget()

show()
chk_lab = Label(root, text="", font=(
    "Kaushan Script", 20), width=10, bg="#deff9c")
chk_lab.pack(pady=10)
time_lab = Label(root, text=nt.ctime(), font=(
    "eufm10", 20), bg="#deff9c", fg="#9000ff")
time_lab.pack(side=BOTTOM)
root.mainloop()
