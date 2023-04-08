
import tkinter as tk
master = tk.Tk()
master.configure(background='cyan')
master.attributes('-fullscreen', True)
master.geometry("400x400")
def open12():
    
    import login
def o9():
    
    import createpage
def openteacher12():
    
    import loginforteachers
def o9teacher():
    
    import createpageteacher

w = tk.Label(master, text="Welcome to", font=("slant","16"))

def exit1():
    master.destroy()
button5 = tk.Button(master,text = "         EXIT         ",font="red",fg="red",command=exit1).place(x=600, y=650)

w.pack()
print(" ")
print(" ")
print(" ")
print(" ")
heading = tk.Label(master, text="EVENT ORGANISER",font=('comicsans',25,'underline'))
heading.pack()


button1 = tk.Button(master,text = "Signup As Student",background="PeachPuff2", foreground="black",font=70,command=o9).place(x=600, y=400)

button2 = tk.Button(master,text = "Login as Student",background="PeachPuff2", foreground="black",font=70, command=open12).place(x=600, y=450)
button3 = tk.Button(master,text = "Signup as Teacher",background="PeachPuff2", foreground="black",font=70,command=o9teacher).place(x=600, y=500)
button4 = tk.Button(master,text = "Login as Teacher",background="PeachPuff2", foreground="black",font=70,command=openteacher12).place(x=600, y=550)
image=tk.PhotoImage(file="pic1final.gif")
tk.Label(master, image=image).pack()

master.mainloop()
