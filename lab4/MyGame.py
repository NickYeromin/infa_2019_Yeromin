from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600') # Размеры окна
canv = Canvas(root,bg='white') # Создание холста и придание фона
canv.pack(fill=BOTH,expand=1) # Размещение по очереди	

colors = ['red','orange','yellow','green','blue'] # БД цветов
def new_ball(): # Функция создания новых цветов
    canv.delete(ALL) # Удаляет все обьекты на холсте
    global x,y,r # Глобальное обьявление переменных
    x = rnd(100,700) # Координата X -рандомное чисто от 100 до 700
    y = rnd(100,500) # Координата Y -рандомное чисто от 100 до 500
    r = rnd(30,50) # Радиус R -рандомное чисто от 30 до 50
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0) # Создание овала
    root.after(1000,new_ball) # Создает новые шары (задержка в МС, что повторять)

def click(event): # Оброботка щелчка мыши
	print(x,y,r)
   # print("Mouse|X=",x," Y=",y," R=",r) # Вывод координат мыши

new_ball() # Запуск создания шаров
canv.bind('<Button-1>', click)
mainloop() # Главный цикл программы