import tkinter.messagebox
from tkinter import *
  
root= Tk()
root.title("Крестики-нолики для двоих")
root.configure(bg="white")

click = True

def show_info():
    tkinter.messagebox.showinfo("Правила игры","Игра ведется на табличке 3х3. У игроков вначале имеется абсолютно пустая таблица, письменная принадлежность и надежда на победу. Один из игроков условно именуется «крестики», другой «нолики». Партию начинает играющий крестиками. Он ставит его на любую из клеточек таблицы. Далее крестиками и ноликами по очереди заполняются свободные клетки. Выигрыш фиксируется, если крестиками или ноликами полностью заполняется вертикаль, горизонталь или диагональ. Победа одного из участников так же фиксируется, если его соперник сдался, убежал, был похищен инопланетянами, или по иным причинам отказывается продолжать игру. ")
    #Источник описания:
    #http://absurdopedia.wikia.com/wiki/%D0%9A%D1%80%D0%B5%D1%81%D1%82%D0%B8%D0%BA%D0%B8-%D0%BD%D0%BE%D0%BB%D0%B8%D0%BA%D0%B8

def checker(buttons):
    global click
    #Если происходит нажатие, то пустое поле меняется на X
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        
    #Если происходит нажатие, то пустое поле меняется на X
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        
    #Выйгрышные комбинации для 0
    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
         button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
         button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
         button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
         button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
         button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
         button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
         button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
         tkinter.messagebox.showinfo("Игра выйграна","Игрок 0 Победил!")
         
    #Выйгрышные комбинации для 0
    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
         button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
         button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
         button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
         button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
         button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
         button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
         button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
         tkinter.messagebox.showinfo("Игра выйграна","Игрок X Победил!")

#Пример разметки поля крестиков-ноликов
         #123
         #456
         #789

#Выйгрышные комбинации в крестиках ноликах:
         #1,2,3(Верхний ряд)
         #4,5,6(Средний ряд)
         #7,8,9(Нижний ряд)
         #3,5,7(Диагональ)
         #1,5,9(Диагональ)
         #1,4,7(Левый Столбец)
         #2,5,8(Средний Столбец)
         #3,6,9(Правый Столбец)

buttons=StringVar()

#Распологаем поле и кнопки
#lambda используется для передачи данных ввода в командную функцию, если у вас есть больше действий для выполнения

button1= Button(root,text=" ",font=("Times 26 bold"), height = 4, width = 8, command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky= S+N+E+W)

button2= Button(root,text=" ",font=("Times 26 bold"), height = 4, width = 8, command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky= S+N+E+W)

button3= Button(root,text=" ",font=("Times 26 bold"), height = 4, width = 8, command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky= S+N+E+W)

button4= Button(root,text=" ",font=("Times 26 bold"), height = 4, width = 8, command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky= S+N+E+W)

button5= Button(root,text=" ",font=("Times 26 bold"), height = 4, width = 8, command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky= S+N+E+W)

button6= Button(root,text=" ",font=("Times 26 bold"), height = 4, width = 8, command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky= S+N+E+W)

button7= Button(root,text=" ",font=("Times 26 bold"), height = 4, width = 8, command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky= S+N+E+W)

button8= Button(root,text=" ",font=("Times 26 bold"), height = 4, width = 8, command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky= S+N+E+W)

button9= Button(root,text=" ",font=("Times 26 bold"), height = 4, width = 8, command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky= S+N+E+W)

#Кнопка выхода 
button_exit= Button(root, text="Выйти",command=quit)
button_exit.grid(row=4, column=2, sticky=E)

#Показывает сообщение внизу экрана c инструкцией
info_message= Button(root, text="?",command=show_info)
info_message.grid(row=4, column=0, sticky=W)

root.mainloop()


         
         
         
    
    
