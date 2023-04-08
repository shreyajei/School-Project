import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import *
import datetime
from datetime import date
import login

master = tk.Toplevel()

master.configure(background='light yellow')
master.attributes('-fullscreen', True)
master.geometry("400x400")
heading = tk.Label(master, text="DANCE",font=('comicsans',25,'bold '),bg="light yellow")
heading.pack()


image = tk.PhotoImage(file="dance.gif")
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
w=tk.Label(master, text="”Dance is the hidden language of the soul”",font=("Times", "18", "bold italic"),bg="light yellow")  
w.pack()
button1 = tk.Button(master,text = "View students enrolled",font=("bold")).place(x=50, y=400)
button2 = tk.Button(master,text = "Delete Your Name From Event",font=("bold")).place(x=600, y=400)

button4 = tk.Button(master,text = "Click here for  further details!",font=("bold")).place(x=300, y=400)

button5 = tk.Button(master,text = "Join event",font=("bold")).place(x=900, y=400)


import datetime
from datetime import date

today = date.today()
date1="08/2/2022"
tk.Label(master, text=date1)

format_str = '%d/%m/%Y' # The format
datetime_obj = datetime.datetime.strptime(date1, format_str)
date2=datetime_obj.date()
def popup():
     tk.Label(master, text="You have successfully been enrolled",fg="green",font=70).place(x=600,y=600)
     button5 = tk.Button(master,text = "Join event ",font=("bold"),state=tk.NORMAL).place(x=900,y=400)
if  date2<=today :
    tk.Label(master, text="The event enrollment date has elapsed",fg="red",font=70).place(x=600,y=600)
    button5 = tk.Button(master,text = "Join event ",font=("bold"),state=tk.DISABLED).place(x=900, y=400)

elif date2>today:
    def getdatacreate1():
        f=login.e1.get()
        print(f)
        #Connection to MySQL Server
        con = mysql.connector.connect(host="localhost", user="root", passwd="sql123")
        mycursor = con.cursor()
        #Creating Student Database
        mycursor.execute("DROP DATABASE IF EXISTS student")
        mycursor.execute("USE project")
        #Creating Studentinfo Table
        sql_query = "SELECT * FROM dance"
        mycursor.execute(sql_query)
    
        result = mycursor.fetchall()
        for (a,) in result:
            if (str(a)==str(f)):
                tk.Label(master, text="You have already been enrolled",fg="red",font=70).place(x=600,y=600)
                button5 = tk.Button(master,text = "Join event ",font=("bold"),state=tk.DISABLED).place(x=900, y=400)
                break;
        else:
            #mycursor.execute("CREATE TABLE dance(name VARCHAR(30))")
            #Inserting Rows in to the table
            st="insert into dance values('" + f + "')"
            print(st)
            mycursor.execute(st)
            button5 = tk.Button(master,text = "Join event ",font=("bold"),state=tk.NORMAL).place(x=900,y=400)
            popup()
        
        con.commit()

    button5 = tk.Button(master,text = "Join event ",font=("bold"),state=tk.NORMAL,command=getdatacreate1).place(x=900,y=400)   


def exit1():
    master.destroy()
button2 = tk.Button(master,text = "EXIT",font=("bold"),command=exit1).place(x=1100, y=400)
#removing name from list
def deletename():
 
    f=login.e1.get()
    con = mysql.connector.connect(host="localhost", user="root", passwd="sql123",database="project")
    mycursor = con.cursor()
    sql_query = "SELECT * FROM dance"
    mycursor.execute(sql_query)
    
    result = mycursor.fetchall()
    for (a,) in result:
        if (str(a)==str(f)):
            #mycursor.execute("CREATE TABLE art(name VARCHAR(30))")
            #Inserting Rows in to the table
            que="delete from dance where name='"+ f +"'"
            print(que)
            mycursor.execute(que)
            print("deleted")
            tk.Label(master, text="You have successfully removed your name",fg="green",font=70).place(x=600,y=600)
            button2 = tk.Button(master,text = "Delete Your Name From Event",font=("bold"),state=tk.NORMAL).place(x=600, y=400)
            
            break;
    else:
        tk.Label(master, text="Your username does not exist in this event",fg="red",font=70).place(x=600,y=600)
        button2 = tk.Button(master,text = "Delete Your Name From Event",font=("bold"),state=tk.DISABLED).place(x=600, y=400)
    con.commit()
    
    
button2 = tk.Button(master,text = "Delete Your Name From Event",font=("bold"),command=deletename).place(x=600, y=400)


    


def view():
    master =tk.Tk()
    
    con = mysql.connector.connect(host="localhost", user="root", passwd="sql123",database="project")
    mycursor = con.cursor()
    sql_query = "select t1.* from studentinfo1 t1, dance t2 where t1.username=t2.name;"
    
    mycursor.execute(sql_query)
    i=0
    for student in mycursor:
        for j in range(0,(len(student)-2)):
            f = Entry(master, width=20, fg='blue')
            f.grid(row=i, column=j)
            f.insert(END, student[j])
        i=i+1
button1 = tk.Button(master,text = "View students enrolled",font=("bold"),command=view).place(x=50, y=400)

def viewdetails():
    import viewdetailspagestudents
    
button4 = tk.Button(master,text = "Click here for  further details!",font=("bold"),command=viewdetails).place(x=300, y=400)

master.mainloop() 
