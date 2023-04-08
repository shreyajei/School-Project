
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
master = tk.Tk() 
master.attributes('-fullscreen', True)
master.geometry("400x400")
master.configure(background='cyan')
 


w = tk.Label(master, text="EVENT ORGANISER",font=('comicsans',25))
ttk.Label(master, text="Enter username",font=40).grid(row=10)
ttk.Label(master, text="Password",font=40).grid(row=11)
ttk.Label(master, text = "Confirm the event you want to coordinate :",  font =40).grid(row = 12,padx=10,pady=25)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)


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
  
eventschosen.grid(column = 1, row = 12) 




button2 = tk.Button(master,text="next",fg="black",state=tk.DISABLED,width=15, height=2).place(x=556, y=650)

 
def getdata():
    username=e1.get()
    
    password=e2.get()
    event=eventschosen.get()
    
   
    print(username,password,event)
    con = mysql.connector.connect(host="localhost", user="root", passwd="sql123")
    mycursor = con.cursor()
    mycursor.execute("USE project")
    sql_query = "SELECT * FROM teacherinfo1"
    mycursor.execute(sql_query)
    result = mycursor.fetchall()
    for (f,p,m,n,) in result:
        if((p==username)and (m==password) and (n==event)):
            button2 = tk.Button(master,text="next",fg="black",state=tk.NORMAL,width=15, height=2,command=open1234).place(x=556, y=650)
            
            tk.Label(master, text="Successful,password matched",fg="green",font=70).place(x=400,y=400)
            break;
    else:
        tk.Label(master, text="Credentials not matched",fg="red",font=70).place(x=400,y=400)
        button2 = tk.Button(master,text="next",fg="black",state=tk.DISABLED,width=15, height=2).place(x=556, y=650)
        
    con.commit()
buttonsubmit = tk.Button(master,text="submit",fg="black",width=15, height=2,command=getdata).place(x=550, y=450)       

def open1234():
    master.withdraw()
    event=eventschosen.get()
    if event=='Art':
        import artteacher
    elif event=='Dance':
        import danceteachers
    elif event=='Music':
        import musicteacher
    elif event=='Quiz':
        import quizteacher
    elif event=='Theatre':
        import theatreteacher
      


master.wait_window()
master.mainloop()

 
