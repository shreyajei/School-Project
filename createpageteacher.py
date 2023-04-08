import mysql.connector
import getpass
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Creating tkinter window 
master = tk.Tk() 
master.attributes('-fullscreen', True)
master.geometry("400x400")
master.configure(background='cyan')
# Label 


ttk.Label(master, text="Enter fullname",font=40).grid(row=10)

ttk.Label(master, text="Enter username",font=40).grid(row=11)
ttk.Label(master, text="Password",font=40).grid(row=12)
ttk.Label(master, text = "Select the event you want to coordinate :",  font = ("Times New Roman", 10)).grid(row = 13,padx=10,pady=25)
e1 = ttk.Entry(master)
e2 = ttk.Entry(master)
e3 = ttk.Entry(master)
#e4 = ttk.Entry(master)

e1.grid(row=10, column=1)
e2.grid(row=11, column=1)
e3.grid(row=12, column=1)



  
n = tk.StringVar() 
eventschosen = ttk.Combobox(master, width = 17,state="readonly",textvariable = n) 
  
# Adding combobox drop down list 
eventschosen['values'] = ('Art',
                          'Dance',
                          'Music',
                          'Quiz',
                          'Theatre') 
  
eventschosen.grid(column = 1, row = 13)
button2 = tk.Button(master,text="next",fg="black",state=tk.DISABLED,width=15, height=2).place(x=556, y=650)

def getdatacreate():
    f=e1.get()
    p=e2.get()
    m=e3.get()
    n=eventschosen.get() 
    
    print(f,p,m,n)
    #Connection to MySQL Server
    con = mysql.connector.connect(host="localhost", user="root", passwd="sql123")
    mycursor = con.cursor()
    
    #Creating Student Database
    #mycursor.execute("DROP DATABASE IF EXISTS student")
    mycursor.execute("USE project")
    #Creating Studentinfo Table
    sql_query = "SELECT * FROM teacherinfo1"
    mycursor.execute(sql_query)
    
    result = mycursor.fetchall()
    for (a,b,c,s,) in result:
        if (b==p):
            tk.Label(master, text="Credentials matching,please change",fg="red",font=70).place(x=400,y=400)
            button2 = tk.Button(master,text="next",fg="black",state=tk.DISABLED,width=15, height=2).place(x=556, y=650)
            break;
    else:
        tk.Label(master, text=" your account has been successfully created",fg="green",font=70).place(x=400,y=400)
        button2 = tk.Button(master,text="next",fg="black",state=tk.NORMAL,width=15, height=2,command=open1234).place(x=556, y=650)
       #mycursor.execute("CREATE TABLE teacherinfo1(name VARCHAR(30),username VARCHAR(30),password VARCHAR(20),event VARCHAR(10))")
        #Inserting Rows in to the table
        st="insert into teacherinfo1 values('" + f+ "'"+",'"+p+"','" + m+ "'"+",'" + n+ "')"
        print(st)
        mycursor.execute(st)
    
    con.commit()

buttonsubmit = tk.Button(master,text="submit",fg="black",width=15, height=2,command=getdatacreate).place(x=550, y=450)    
    

def open1234():
    master.withdraw()
    import loginforteachers

master.mainloop()



 
