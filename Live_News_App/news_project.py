from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import json
import requests
import pyttsx3
import sys
root = Tk()
root.geometry('550x500')
root.resizable(0,0)
root.title("Live News App::  #Develope By :: Ankush Verma")
root.config(background = "#daeb26")
top_panel = Frame(root, width = 550, height = 100, bg = "#daeb26")
top_panel.pack(side = TOP)
mid_panel = Frame(root, width = 500, height = 200, bg = "#daeb26")
mid_panel.pack(pady = 5)
bottom_panel = Frame(root, width = 550, height = 150, bg = "#daeb26")
bottom_panel.pack(pady = 10)
lower_bottom_panel = Frame(root, width = 550, height = 50, bg = "#daeb26")
lower_bottom_panel.pack()


right_arrow_img = PhotoImage(file = "D:\\Python\\Live_News_App\\right-arrow.png")
left_arrow_img = PhotoImage(file = "D:\\Python\\Live_News_App\\left-arrow.png")
microphone_img = PhotoImage(file = "D:\\Python\\Live_News_App\\microphone.png")
muted_img = PhotoImage(file = "D:\\Python\\Live_News_App\\muted.png")
next_img = PhotoImage(file = "D:\\Python\\Live_News_App\\next.png")
back_img = PhotoImage(file = "D:\\Python\\Live_News_App\\back.png")
reload_img = PhotoImage(file = "D:\\Python\\Live_News_App\\reload(2).png")
exit_img = PhotoImage(file = "D:\\Python\\Live_News_App\\exit(2).png")

news_url = requests.get("https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=67add21c95e543b08ca65a938fb5e155")
json_data = json.loads(news_url.text)

#--------------------------------------------
head_list,main_content_list, image_url_list =[], [], []
except_index = 10
for i in range(0,except_index):
    if str((json_data['articles'][i]['title'])) != "None" and str((json_data['articles'][i]['description'])) != "None" and str((json_data['articles'][i]['urlToImage'])) != "None":
        head_list.append((json_data['articles'][i]['title']))
        main_content_list.append((json_data['articles'][i]['description']))
        image_url_list.append(requests.get(json_data['articles'][i]['urlToImage']))
    else:
        if except_index > 0:
            except_index -=1
        continue
    
#--------------------------------------------


head = head_list[0]
main_content = main_content_list[0]

image_url = image_url_list[0]
img = Image.open(BytesIO(image_url.content))
index = 0

def next_fun():
    global head, main_content, image_url, index, img_new
    index +=1
    if index < except_index:
        head = head_list[index]
        main_content = main_content_list[index]
        image_url = image_url_list[index]
        img_new = Image.open(BytesIO(image_url.content))
    if index >= except_index:
        header_lbl.config(text = "Oops News are finished ,try Later for latest news")
        index = except_index
        next_news_btn.pack_forget()
        exit_btn.pack(side = RIGHT, padx = 10)
    return head,main_content,image_url,img_new

def back_fun():
    global head, main_content, image_url, index, img_new
    if index > 0:
        index -=1
        head = head_list[index]
        main_content = main_content_list[index]
        image_url = image_url_list[index]
        img_new = Image.open(BytesIO(image_url.content))
        exit_btn.pack_forget()
        next_news_btn.pack(side = RIGHT, padx = 10)
        header_lbl.config(text = "Live Breaking News::Powered By Google")
        return head,main_content,image_url,img_new

def exit_fun():
    sys.exit()
#---------------------------------------------

if len(head) >= 50:
    head1 = head[0:46]

nxt_line , last_line= 45 , 45
headline_len = len(head)

def right_btn_fun():
    global nxt_line, headline_len, last_line
    nxt_line+=10
    if nxt_line <= headline_len:
        last_line+=10
        head_new = head[:nxt_line]
        head_lbl.config(text = str(head_new))
        if nxt_line >= (headline_len - 10):
            head_new = head[(last_line-45):]
            head_lbl.config(text = str(head_new))
            right_btn.pack_forget()
            nxt_line,last_line = 45 , 45
            left_btn.pack(side = LEFT)

def left_btn_fun():
    head_new3 = head[:46]
    head_lbl.config(text = str(head_new3))
    left_btn.pack_forget()
    right_btn.pack(side = RIGHT)

if len(main_content) >= 50:
    main_content_data = main_content[:46]

main_content_len = len(main_content)

def main_right_btn_fun():
    global nxt_line, main_content_len, last_line
    nxt_line+=10
    if nxt_line <= main_content_len:
        last_line+=10
        main_content_new = main_content[:nxt_line]
        main_lbl.config(text = str(main_content_new))
        if nxt_line >= (main_content_len - 10):
            main_content_new = main_content[(last_line-45):]
            main_lbl.config(text = str(main_content_new))
            main_right_btn.pack_forget()
            nxt_line,last_line = 45 , 45
            main_left_btn.pack(side = LEFT)


def main_left_btn_fun():
    main_content_new2 = main_content[:46]
    main_lbl.config(text = str(main_content_new2))
    main_left_btn.pack_forget()
    main_right_btn.pack(side = RIGHT)
num = 1
def mic_fun():
    global num, head, main_content
    num +=1
    if num%2 == 0:
        mic_btn.config(image = muted_img, bd = 3, relief = SUNKEN)
        engine = pyttsx3.init()
        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
        rate = engine.getProperty('rate')   
        engine.setProperty('rate', 125)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', ru_voice_id)
        engine.say("Headlines "+str(head))
        engine.say("Main News "+str(main_content))
        engine.runAndWait()

    else:
        mic_btn.config(image = microphone_img, bd = 3, relief = RAISED)

def reload_fun():
    main_left_btn_fun()
    left_btn_fun()
    img_new = Image.open(BytesIO(image_url.content))
    size = (500,200)
    img_new.thumbnail(size)
    new_img1 = ImageTk.PhotoImage(img_new)
    news_img.config(image = new_img1)
    news_img.image = new_img1


size = (500,200)
img.thumbnail(size)
new_img = ImageTk.PhotoImage(img)
header_lbl = Label(top_panel, text = "Live Breaking News::Powered By Google",font = ("Arial Bold",10), bg = "#daeb26", fg = "#ff0505")
header_lbl.pack(side = TOP, pady = 5)
head_lbl = Label(top_panel, text = str(head)+"...", font = ("Arial Bold",15), bg = "#daeb26", fg = "#7f15bd")
head_lbl.pack()
left_btn = Button(top_panel, image = left_arrow_img, bg = "#daeb26", bd = 0, command = left_btn_fun)
left_btn.pack(side = LEFT)
right_btn = Button(top_panel, image = right_arrow_img, bg = "#daeb26", bd = 0, command = right_btn_fun)
right_btn.pack(side = RIGHT)
news_img = Label(mid_panel, image = new_img)
news_img.pack()
desc_lbl = Label(bottom_panel, text = "Description :", font = ("Allura",25), fg = "red", bg = "#daeb26")
desc_lbl.pack()
main_lbl = Label(bottom_panel, text = str(main_content_data), font = ("KaushanScript",20), fg = "#a11069" ,bg = "#daeb26")
main_lbl.pack()
main_right_btn = Button(bottom_panel, image = right_arrow_img, bg = "#daeb26", bd = 0, command = main_right_btn_fun)
main_right_btn.pack(side = RIGHT)
main_left_btn = Button(bottom_panel, image = left_arrow_img, bg = "#daeb26", bd = 0, command = main_left_btn_fun)
main_left_btn.pack(side = LEFT)
back_news_btn = Button(lower_bottom_panel,text = "Back", image = back_img, compound = "left", bd = 0, bg = "#daeb26", command = back_fun)
back_news_btn.pack(side = LEFT, padx = 10)
reload_btn = Button(lower_bottom_panel, image = reload_img, bd = 3,relief = RAISED, bg = "#b0e83f", command = reload_fun)
reload_btn.pack(side = LEFT, padx = 10, ipadx = 5, ipady = 5)
mic_btn = Button(lower_bottom_panel, image = microphone_img, bd = 3,relief = RAISED, bg = "#b0e83f", command = mic_fun)
mic_btn.pack(side = LEFT, padx = 10, ipadx = 5, ipady = 5)
next_news_btn = Button(lower_bottom_panel, text = "Next", image = next_img, compound = "right", bd = 0, bg = "#daeb26", command = next_fun)
next_news_btn.pack(side = RIGHT, padx = 10)
exit_btn = Button(lower_bottom_panel, image = exit_img, bd = 0, bg = "#daeb26", command = exit_fun)
root.mainloop()