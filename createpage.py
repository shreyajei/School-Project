import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import getpass
master = tk.Tk()
master.configure(background='cyan')
master.attributes('-fullscreen', True)
master.geometry("400x400")
w = tk.Label(master, text="EVENT ORGANISER",font=('comicsans',25))
tk.Label(master, text=" Enter fullname",bg="light yellow",font=40).grid(row=10)
tk.Label(master, text=" Enter age",bg="light yellow",font=40).grid(row=11)
tk.Label(master, text=" Enter gender",bg="light yellow",font=40).grid(row=12)
tk.Label(master, text=" Enter house",bg="light yellow",font=40).grid(row=13)
tk.Label(master, text=" Enter username",bg="light yellow",font=40).grid(row=14)
tk.Label(master, text=" Enter password",bg="light yellow",font=40).grid(row=15)


 
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)

e1.grid(row=10, column=1)
e2.grid(row=11, column=1)
e3.grid(row=12, column=1)
e4.grid(row=13, column=1)
e5.grid(row=14, column=1)
e6.grid(row=15, column=1)



m = tk.StringVar() 
gender = ttk.Combobox(master, width = 17,state="readonly",  
                            textvariable = m) 
  
# Adding combobox drop down list 
gender['values'] = ('M',
                          'F') 
gender.grid(column = 1, row = 12)    
n = tk.StringVar() 
house = ttk.Combobox(master, width = 17,state="readonly",  
                            textvariable = n) 
  
# Adding combobox drop down list 
house['values'] = ('Explorers',
                          'Challengers',
                          'Pioneers',
                          'Voyagers') 
  
house.grid(column = 1, row = 13) 

button2 = tk.Button(master,text="next",fg="black",state=tk.DISABLED,width=15, height=2).place(x=556, y=650)
def getdatacreate():
    f=e1.get()
    p=e2.get()
    m=gender.get()
    n=house.get() 
    t=e5.get()
    d=e6.get()
    print(f,p,m,n,t,d)
    #Connection to MySQL Server
    con = mysql.connector.connect(host="localhost", user="root", passwd="sql123")
    mycursor = con.cursor()
    
    #Creating Student Database
    #mycursor.execute("DROP DATABASE IF EXISTS student")
    mycursor.execute("USE project")
    sql_query = "SELECT * FROM studentinfo1"
    mycursor.execute(sql_query)
    
    result = mycursor.fetchall()
    for (a,b,c,s,u,w,) in result:
        if (u==t):
            tk.Label(master, text="Credentials matching,please change",fg="red",font=70).place(x=400,y=400)
            button2 = tk.Button(master,text="next",fg="black",state=tk.DISABLED,width=15, height=2).place(x=556, y=650)
            break;
    else:
        tk.Label(master, text=" Your account has been successfully created",fg="green",font=70).place(x=400,y=400)
        button2 = tk.Button(master,text="next",fg="black",state=tk.NORMAL,width=15, height=2,command=open1234).place(x=556, y=650)
        st="insert into studentinfo1 values('" + f+ "'"+","+p+",'" + m+ "'"+",'" + n+ "'"+",'" + t+ "','" + d+ "')"
        print(st)
        mycursor.execute(st)
        
        
    #Creating Studentinfo Table
        con.commit()
    
#mycursor.execute("CREATE TABLE studentinfo1(name VARCHAR(30),age INT(3),gender VARCHAR(10),house VARCHAR(14),username VARCHAR(6),password VARCHAR(8))")
    #Inserting Rows in to the table
     

buttonsubmit = tk.Button(master,text="submit",fg="black",width=15, height=2,command=getdatacreate).place(x=550, y=450)    
    

def open1234():
    master.withdraw()
    import login
    


master.mainloop()
