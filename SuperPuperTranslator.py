#-*-coding: 1251-*-

from tkinter import *
from googletrans import Translator 
import pyperclip

def Clear(): 
    #global count 
    #count = 0 
    open('history.txt', 'w').close()

def Write():
    #global count
    #count += 1
    #text = f"{count} ввод: \nВы ввели:{t.get('1.0', END)}Перевод: {t1.get('1.0', END)}"
    text = f"{count} ввод: \nВы ввели:{t.get('1.0', END)}Перевод: {t1.get('1.0', END)}"
    
    with open("history.txt", "a") as file:
        file.write(text)

def Clipboard(): 
    pyperclip.copy(t1.get('1.0', END))
    


def Tran():
    text = t.get('1.0', END)
    
    translator = Translator()
    
    translation = translator.translate(text, dest='en')
    
    
    t1.delete('1.0', END)
    t1.insert('1.0', translation.text)

root = Tk()
root.geometry('500x490')
root.title('Переводчик')
root.resizable(width=False, height=False)
root['bg'] = 'blue'


label = Label(root, fg='black', bg='white', font='Arial 15 bold', text='Введите текст на русском') #говно ебаное, не вставить русский текст
label.place(relx=0.5, y=30, anchor=CENTER)
t = Text(root, width=35, height=5, font='Arial 12 bold')
t.place(relx=0.5, y=100, anchor=CENTER)


btn = Button(root, width=45, text='Перевести', command=Tran)
btn.place(relx=0.5, y=180, anchor=CENTER)

t1 = Text(root, width=35, height=5, font='Arial 12 bold') 
t1.place(relx=0.5, y=260, anchor=CENTER)

btn2 = Button(root, width=55, text='В буфер обмена', command=Clipboard)
btn2.place(relx=0.5, y=340, anchor=CENTER)

count = 0
btn3 = Button(root, width=55, text='История файлов', command=Write)
btn3.place(relx=0.5, y=400, anchor=CENTER)

btn4 = Button(root, width=55, text='Очистка историти файлов', command=Clear)
btn4.place(relx=0.5, y=460, anchor=CENTER)

root.mainloop()


