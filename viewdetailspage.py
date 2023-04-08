import tkinter as tk
import loginforteachers as lft
master = tk.Tk() 
master.configure(background='cyan')
master.geometry("400x400")
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", passwd="sql123",database="project")
mycursor = con.cursor()
mycursor.execute("select event from teacherinfo1 where username='"+lft.e1.get()+"'")
a=mycursor.fetchall()
mycursor.execute("select * from eventdetails where event='"+a[0][0]+"'")
data=mycursor.fetchone()

tk.Label(master,font=40,text="Date of event-"+str(data[1])).grid(row=10)
tk.Label(master,font=40,text="Venue        -"+str(data[2])).grid(row=12)
tk.Label(master,font=40, text="Period No    -"+str(data[3])).grid(row=14)

master.mainloop()
