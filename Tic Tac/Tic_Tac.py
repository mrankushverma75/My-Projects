import os
from tkinter import *
root = Tk()
root.title("Game")
root.geometry('500x500')
root.resizable(0,0)
n=1
def show(e):
    global n
    n+=1
    if (n%2==0):
        if (e["text"]==""):
            e["text"]="X"
    else:
        if (e["text"]==""):
            e["text"]="O"

    if (button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        print("1st Player is Winner!!!")
        button1.configure(background="blue",fg="white")
        button2.configure(background="blue",fg="white")
        button3.configure(background="blue",fg="white")
        button5["text"]="GAME OVER\nPlayer 1"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()

    if (button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        print("2nd Player is Winner!!!")
        button1.configure(background="red",fg="white")
        button2.configure(background="red",fg="white")
        button3.configure(background="red",fg="white")
        button5["text"]="GAME OVER\nPlayer 2"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()


    if (button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        print("1st Player is Winner!!!")
        button4.configure(background="blue",fg="white")
        button5.configure(background="blue",fg="white")
        button6.configure(background="blue",fg="white")
        button5["text"]="GAME OVER\nPlayer 1"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()


    if (button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        print("2nd Player is Winner!!!")
        button4.configure(background="red",fg="white")
        button5.configure(background="red",fg="white")
        button6.configure(background="red",fg="white")
        button5["text"]="GAME OVER\nPlayer 2"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()


    
    if (button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        print("1st Player is Winner!!!")
        button7.configure(background="blue",fg="white")
        button8.configure(background="blue",fg="white")
        button9.configure(background="blue",fg="white")
        button5["text"]="GAME OVER\nPlayer 1"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()

    if (button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        print("2nd Player is Winner!!!")
        button7.configure(background="red",fg="white")
        button8.configure(background="red",fg="white")
        button9.configure(background="red",fg="white")
        button5["text"]="GAME OVER\nPlayer 2"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()



    if (button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        print("1st Player is Winner!!!")
        button1.configure(background="blue",fg="white")
        button4.configure(background="blue",fg="white")
        button7.configure(background="blue",fg="white")
        button5["text"]="GAME OVER\nPlayer 1"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()


    if (button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        print("2nd Player is Winner!!!")
        button1.configure(background="red",fg="white")
        button4.configure(background="red",fg="white")
        button7.configure(background="red",fg="white")
        button5["text"]="GAME OVER\nPlayer 2"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()


    if (button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        print("1st Player is Winner!!!")
        button2.configure(background="blue",fg="white")
        button5.configure(background="blue",fg="white")
        button8.configure(background="blue",fg="white")
        button5["text"]="GAME OVER\nPlayer 1"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()


    if (button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        print("2nd Player is Winner!!!")
        button2.configure(background="red",fg="white")
        button5.configure(background="red",fg="white")
        button8.configure(background="red",fg="white")
        button5["text"]="GAME OVER\nPlayer 2"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()


    if (button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        print("1st Player is Winner!!!")
        button3.configure(background="blue",fg="white")
        button6.configure(background="blue",fg="white")
        button9.configure(background="blue",fg="white")
        button5["text"]="GAME OVER\nPlayer 1"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()


    if (button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        print("2nd Player is Winner!!!")
        button3.configure(background="red",fg="white")
        button6.configure(background="red",fg="white")
        button9.configure(background="red",fg="white")
        button5["text"]="GAME OVER\nPlayer 2"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()


    if (button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        print("1st Player is Winner!!!")
        button1.configure(background="blue",fg="white")
        button5.configure(background="blue",fg="white")
        button9.configure(background="blue",fg="white")
        button5["text"]="GAME OVER\nPlayer 1"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()

    if (button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        print("2nd Player is Winner!!!")
        button1.configure(background="red",fg="white")
        button5.configure(background="red",fg="white")
        button9.configure(background="red",fg="white")
        button5["text"]="GAME OVER\nPlayer 2"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()


    if (button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        print("1st Player is Winner!!!")
        button3.configure(background="blue",fg="white")
        button5.configure(background="blue",fg="white")
        button7.configure(background="blue",fg="white")
        button5["text"]="GAME OVER\nPlayer 1"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()
    if (button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        print("2nd Player is Winner!!!")
        button3.configure(background="red",fg="white")
        button5.configure(background="red",fg="white")
        button7.configure(background="red",fg="white")
        button5["text"]="GAME OVER\nPlayer 2"
        button5["background"]="Yellow"
        button5["font"]=("Algerian",10)
        button5["fg"]="red"
        os._exit()
    

button1=Button(root, text="",height="10",width="20", command= lambda:show(button1))
button1.grid(row=0, column=0)
button2=Button(root, text="",height="10",width="20", command= lambda:show(button2))
button2.grid(row=0, column=1)
button3=Button(root, text="",height="10",width="20", command= lambda:show(button3))
button3.grid(row=0, column=2)

button4=Button(root, text="",height="10",width="20", command= lambda:show(button4))
button4.grid(row=1, column=0)
button5=Button(root, text="",height="10",width="20", command= lambda:show(button5))
button5.grid(row=1, column=1)
button6=Button(root, text="",height="10",width="20", command= lambda:show(button6))
button6.grid(row=1, column=2)

button7=Button(root, text="",height="10",width="20", command= lambda:show(button7))
button7.grid(row=2, column=0)
button8=Button(root, text="",height="10",width="20", command= lambda:show(button8))
button8.grid(row=2, column=1)
button9=Button(root, text="",height="10",width="20", command= lambda:show(button9))
button9.grid(row=2, column=2)

root.mainloop()