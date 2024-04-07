from tkinter import Tk , Entry , Button , StringVar
import tkinter as tk

root = Tk()
root.title('Simple Calculator')
root.geometry('300x400')
root.resizable(width=0, height=0)
root.configure(bg='black')
e = Entry(root, bd=10, width=30, font='Arial 21', bg='lightgreen')
e.pack()
def click(number):
    e.insert(index=32, string=number)
def add():
    e.insert(index=32, string="+")

def clear():
    e.delete(0, tk.END) 

def equal():
    current = e.get()
    list = current.split("+")  
    result =( int(list[0]) + int(list[1])) 
    clear()
    e.insert(index=32, string=result)  


btn1 = Button(root, text='7', font='Arial 19 bold', bg='grey', bd=10, padx=10, pady=5, command=lambda: click(7))
btn1.place(x=10,y=60)
btn2 = Button(root, text='8', font='Arial 19 bold', bg='grey', bd=10, padx=10, pady=5, command=lambda: click(8))
btn2.place(x=85,y=60)
btn3 = Button(root, text='9', font='Arial 19 bold', bg='grey', bd=10, padx=10, pady=5, command=lambda: click(9))
btn3.place(x=160,y=60)
btn4 = Button(root, text='4', font='Arial 19 bold', bg='grey', bd=10, padx=10, pady=5, command=lambda: click(4))
btn4.place(x=10,y=145)
btn5 = Button(root, text='5', font='Arial 19 bold', bg='grey', bd=10, padx=10, pady=5, command=lambda: click(5))
btn5.place(x=85,y=145)
btn6 = Button(root, text='6', font='Arial 19 bold', bg='grey', bd=10, padx=10, pady=5, command=lambda: click(6))
btn6.place(x=160,y=145)
btn7 = Button(root, text='1', font='Arial 19 bold', bg='grey', bd=10, padx=10, pady=5, command=lambda: click(1))
btn7.place(x=10,y=230)
btn8 = Button(root, text='2', font='Arial 19 bold', bg='grey', bd=10, padx=10, pady=5, command=lambda: click(2))
btn8.place(x=85,y=230)
btn9 = Button(root, text='3', font='Arial 19 bold', bg='grey', bd=10, padx=10, pady=5, command=lambda: click(3))
btn9.place(x=160,y=230)
btn10 = Button(root, text='0', font='Arial 19 bold', bg='grey', bd=10, padx=10, pady=5, command=lambda: click(0))
btn10.place(x=10,y=320)

btn11 = Button(root, text='+', font='Arial 19 bold', bg='skyBlue', bd=10,height=4, command=add)
btn11.place(x=235,y=60)

btn12 = Button(root, text='C', font='Arial 19 bold', bg='Crimson', bd=10,height=1, width=8, command=clear)
btn12.place(x=85,y=320)

btn13 = Button(root, text='=', font='Arial 19 bold', bg='khaki', bd=10, height=4, command=equal)
btn13.place(x=235,y=230)























root.mainloop()