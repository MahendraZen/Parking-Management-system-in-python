
from tkinter import *
from tkinter import messagebox
import sqlite3
import os
root=Tk()

conn =sqlite3.connect('index.db')
c = conn.cursor()
#c.execute('CREATE TABLE users(name text,regNo text, gender text, mobile text, email text, password text,block text,price text)')
root.geometry("500x500")
root.title('SIGN UP')
frame_1=Frame(root)
frame_1.configure(background="#00C0E4")
root.configure(background="#00C0E4")

def redg():
    print ("Please register!")
    name = e1.get()
    regNO = e6.get()
    gender=var.get()
    mobile = e3.get()
    email = e4.get()
    password = e5.get()
    print(name)
    print(regNO)
    print(mobile)
    print(email)
    print(password)
    
    if((name== "") or (regNO=="") or (mobile == "") or (email == "") or (password == "")  ):
        print('Empty')
        messagebox.showerror("Details","Please enter the details")
    else:
        print('We got you')
        listdata = (name,regNO,gender ,mobile, email, password,'','')
        c.execute('INSERT INTO users VALUES(?,?,?,?,?,?,?,?)',listdata)
        c.execute('SELECT * FROM users')
        data = c.fetchall()
        for i in data:
            print(i)
        conn.commit()
        conn.close()
        messagebox.showinfo("Detail","Registration successful")
        os.popen('py login.py')
        global root
        root.quit()

def can():
    root.destroy()

l0=Label(frame_1,text="Register",bg="#00C0E4",fg="#212121")
l0.config(font=('algerian', 30))
l1=Label(frame_1,text="Name:",bg="#00C0E4",fg="#212121")
l1.config(font=('algerian', 15))
l2=Label(frame_1,text="Gender:",bg="#00C0E4",fg="#212121")
l2.config(font=('algerian', 15))
l3=Label(frame_1,text="Mobile No:",bg="#00C0E4",fg="#212121")
l3.config(font=('algerian', 15))
l4=Label(frame_1,text="Email ID:",bg="#00C0E4",fg="#212121")
l4.config(font=('algerian', 15))
l5=Label(frame_1,text="Password:",bg="#00C0E4",fg="#212121")
l5.config(font=('algerian', 15))
l6=Label(frame_1,text="Reg No:",bg="#00C0E4",fg="#212121")
l6.config(font=('algerian', 15))
e1=Entry(frame_1,bd=1,width="50",)
e6=Entry(frame_1,bd=1,width="50",)
var=IntVar()
r1=Radiobutton(frame_1,text="Male",variable=var,value=1,bg="#00C0E4",fg="#212121")
r2=Radiobutton(frame_1,text="Female",variable=var,value=2,bg="#00C0E4",fg="#212121")
e2=Entry(frame_1,bd=1,width="50")
e3=Entry(frame_1,bd=1,width="50")
e4=Entry(frame_1,bd=1,width="50")
e5=Entry(frame_1,bd=1,width="50", show="*")
r1.grid(row=3,column=1)
r2.grid(row=4,column=1)
l0.grid(row=0,column=0)
l1.grid(row=1,column=0)
l6.grid(row=2,column=0)
l2.grid(row=3,column=0)
l3.grid(row=5,column=0)
l4.grid(row=6,column=0)
l5.grid(row=7,column=0)
e1.grid(row=1,column=1)
e6.grid(row=2,column=1)
e5.grid(row=7, column=1)
e3.grid(row=5,column=1)
e4.grid(row=6,column=1)
B2=Button(frame_1,text="Submit",bg="#212121",fg="#fff",command=redg,width="10")
B1=Button(frame_1,text="Cancel",bg="#212121",fg="#fff",width="10",command=can)
B2.grid(row=9,columnspan=2)
B1.grid(row=9,column=1,columnspan=1)

frame_1.grid(row=0,column=0)

root.mainloop()

