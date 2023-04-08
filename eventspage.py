# import everything from tkinter module
import tkinter as tk
import mysql.connector
from tkinter import *    
event='hello'
# create a tkinter window 
root = Tk()               
root.attributes('-fullscreen', True)
root.geometry("400x400") 
# Open window having dimension 100x100
w = tk.Label(root, text="Welcome to Events Page",font=('comicsans',25))
 
root.configure(background='cyan')
w.pack()

def linking():
    global event
    event="art"
    import artpage1
button2 = tk.Button(root,text="Art",fg="black",width=15, height=2,font='calibri',command=linking).place(x=600, y=150)
def linking1():
    global event
    event='dance'
    import dance1
button3 = tk.Button(root,text="Dance",fg="black",width=15, height=2,font='calibri',command=linking1).place(x=600, y=250)

def linking2():
    global event
    event='music'
    import music1
button4 = tk.Button(root,text="Music",fg="black",width=15, height=2,font='calibri',command=linking2).place(x=600, y=350)

def linking3():
    global event
    event='quiz'
    import quiz1
button5 = tk.Button(root,text="Quiz",fg="black",width=15, height=2,font='calibri',command=linking3).place(x=600, y=450)

def linking4():
    global event
    event='theatre'
    import theatre1
button6 = tk.Button(root,text="Theatre",fg="black",width=15, height=2,font='calibri',command=linking4).place(x=600, y=550)

def exit1():
    root.destroy()
button7 = tk.Button(root,text = "EXIT",fg="red",width=15, height=2,font='calibri',command=exit1).place(x=600, y=650)

root.mainloop()
 
