import mysql.connector
import tkinter as tk
import loginforteachers as lft
from tkinter import messagebox
master = tk.Tk()
master.configure(background='cyan')
master.attributes('-fullscreen', True)
master.geometry("400x400")
con = mysql.connector.connect(host="localhost", user="root", passwd="sql123",database="project")
mycursor = con.cursor()
flag1='False'
flag2='False'
flag3='False'
#mycursor.execute("CREATE TABLE eventdetails(event varchar(10) NOT NULL primary key,dateofevent date,venue VARCHAR(30),periodno int)")
#mycursor.execute("insert into eventdetails values('art','12-01-03','art room',4)")
#mycursor.execute("insert into eventdetails values('music','12-01-03','music room',1)")
#mycursor.execute("insert into eventdetails values('theatre','12-01-03','mini audi',2)")
#mycursor.execute("insert into eventdetails values('dance','12-01-03','dance room',9)")
#mycursor.execute("insert into eventdetails values('quiz','12-01-03','av room',6)")

# Open window having dimension 100x100 
master.geometry('100x100')
def getdatadate():
    global flag1
    mycursor.execute("select event from teacherinfo1 where username='"+lft.e1.get()+"'")
    a=mycursor.fetchall()
    mycursor.execute("select dateofevent from eventdetails where event='"+a[0][0]+"'")
    b=mycursor.fetchall()
    return((a,b))
    #print(a)
    #[('Dance',)]
    flag='True'
def getdatavenue():
    global flag2
    mycursor.execute("select event from teacherinfo1 where username='"+lft.e1.get()+"'")
    a=mycursor.fetchall()
    mycursor.execute("select venue from eventdetails where event='"+a[0][0]+"'")
    b=mycursor.fetchall()
    print(b)
    return((a,b))
    #print(a)
    flag='True'
def getdataperiodno():
    global flag3
    mycursor.execute("select event from teacherinfo1 where username='"+lft.e1.get()+"'")
    a=mycursor.fetchall()
    mycursor.execute("select periodno from eventdetails where event='"+a[0][0]+"'")
    b=mycursor.fetchall()
    return((a,b))
    print(b)
    #print(a)
    flag='True'

button1 = tk.Button(master,text="confirm same/new date",fg="black",width=30, height=1,command=getdatadate).place(x=700, y=0)
button2 = tk.Button(master,text="confirm same/new venue",fg="black",width=30, height=1,command=getdatavenue).place(x=700, y=20)
button3 = tk.Button(master,text="confirm same/new period no",fg="black",width=30, height=1,command=getdataperiodno).place(x=700, y=40)

tk.Label(master,font=40,text="Date of event:(in yyyy-mm-dd format").grid(row=10)
tk.Label(master,font=40, text="Venue                             :").grid(row=11)
tk.Label(master,font=40, text="Period No:                         ").grid(row=12)

if flag1!='True':
    e1 = tk.Entry(master)
if flag2!='True':
    e2 = tk.Entry(master)
if flag3!='True':
    e3 = tk.Entry(master)
e1.grid(row=10, column=1)
e2.grid(row=11, column=1)
e3.grid(row=12, column=1)
def submit():
    #when typed in entry box
    con = mysql.connector.connect(host="localhost", user="root", passwd="sql123",database="project")
    mycursor = con.cursor()
    mycursor.execute("USE project")
    if e1.get()!="":
        que="update eventdetails set dateofevent='"+e1.get()+"' where event='"+str(getdatadate()[0][0][0])+"'"
        print(que)
        mycursor.execute(que)
        con.commit()
    if e2.get()!="":
        que="update eventdetails set venue='"+str(e2.get())+"' where event='"+str(getdatadate()[0][0][0])+"'"
        mycursor.execute(que)
        con.commit()
    if e3.get()!="":
        que="update eventdetails set periodno="+e3.get()+" where event='"+str(getdatadate()[0][0][0])+"'"
        mycursor.execute(que)
        con.commit()
    tk.Label(master, text="Details have been changed",fg="red",font=70).place(x=400,y=400)
    
    con.commit()
buttonsubmit = tk.Button(master,text="submit",fg="black",width=15, height=2,command=submit).place(x=550, y=600)
def exit1():
    master.destroy()
button4 = tk.Button(master,text = "         EXIT   ",font="red",fg="red",command=exit1).place(x=550, y=650)

master.wait_window()
master.mainloop()
