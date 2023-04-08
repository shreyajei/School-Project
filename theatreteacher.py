import tkinter as tk
import mysql.connector
from tkinter import *
master = tk.Toplevel()
master.configure(background='light yellow')
master.attributes('-fullscreen', True)
master.geometry("400x400")
heading = tk.Label(master, text="QUIZ",font=('comicsans',25,'bold '),bg="light yellow")
heading.pack()


image = tk.PhotoImage(file="theatre.gif")
tk.Label(master, image=image).pack()

print(" ")
print(" ")
print(" ")
print("\n")
a=tk.Label(master,text="                ",bg="light yellow")
a.pack()
b=tk.Label(master,text="                ",bg="light yellow")
b.pack()
c=tk.Label(master,text="                ",bg="light yellow")
c.pack()
w=tk.Label(master, text="ITS SHOWTIME",font=("Times", "20", "bold italic"),bg="light yellow")  
w.pack()
def view():
    master =tk.Tk()
    
    con = mysql.connector.connect(host="localhost", user="root", passwd="sql123",database="project")
    mycursor = con.cursor()
    sql_query = "select t1.* from studentinfo1 t1, theatre t2 where t1.username=t2.name;"
    
    mycursor.execute(sql_query)
    i=0
    for student in mycursor:
        for j in range(0,(len(student)-2)):
            f = Entry(master, width=20, fg='blue')
            f.grid(row=i, column=j)
            f.insert(END, student[j])
        i=i+1
button1 = tk.Button(master,text = "VIEW",font=("bold"),command=view).place(x=50, y=400)
def linking2():
    import changedetailsteachers
def linking3():
    import viewdetailspage   

def exit1():
    master.destroy()
button2 = tk.Button(master,text = "EXIT",font=("bold"),command=exit1).place(x=550, y=400)

button3 = tk.Button(master,text = "Change details of event",font=("bold"),command=linking2).place(x=150, y=400)
button4 = tk.Button(master,text = "VIEW current details",font=("bold"),command=linking3).place(x=350, y=400)

