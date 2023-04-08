import tkinter as tk
from tkinter import messagebox
import mysql.connector

master = tk.Tk()
master.configure(background='cyan')
master.attributes('-fullscreen', True)
master.geometry("400x400")
w = tk.Label(master, text="EVENT ORGANISER",font=('comicsans',25))
tk.Label(master, text="Enter username",font=40).grid(row=10)
tk.Label(master, text="Password",font=40).grid(row=11)
def open123():
    import eventspage
e1 = tk.Entry(master)
e2 = tk.Entry(master)


e1.grid(row=10, column=1)
e2.grid(row=11, column=1)

button2 = tk.Button(master,text="next",fg="black",state=tk.DISABLED,width=15, height=2).place(x=556, y=650)

def getdata():
    username=e1.get()
    password=e2.get()
    print(username,password)
    con = mysql.connector.connect(host="localhost", user="root", passwd="sql123")
    mycursor = con.cursor()
    mycursor.execute("USE project")
    sql_query = "SELECT * FROM studentinfo1"
    mycursor.execute(sql_query)
    result = mycursor.fetchall()
    for (f,p,m,n,t,d,) in result:
        if (t==username) and (d==password):
            
            tk.Label(master, text="Successful,password matched",fg="green",font=70).place(x=400,y=400)
            button2 = tk.Button(master,text="next",fg="black",state=tk.NORMAL,width=15, height=2,command=open1234).place(x=556, y=650)
            break;
    else:
        tk.Label(master, text="Credentials not matched",fg="red",font=70).place(x=400,y=400)
        button2 = tk.Button(master,text="next",fg="black",state=tk.DISABLED,width=15, height=2).place(x=556, y=650)

        
    con.commit()

buttonsubmit = tk.Button(master,text="submit",fg="black",width=15, height=2,command=getdata).place(x=550, y=450)       

def open1234():
    master.withdraw()
    import eventspage
 

master.wait_window()
master.mainloop()








