from tkinter import *
from tkinter import messagebox
import sqlite3
import os
conn = sqlite3.connect('index.db')
c = conn.cursor()
def redg():
    os.popen('py signup.py')
    window1.destroy()
def log():
    res = 0
    err = 0
    regNO = Entry_1.get()
    password = Entry_2.get()
    if((regNO == "") or (password == "")):
        print('Inputs Empty')
        messagebox.showerror("Details","Please enter the details")
    else:
        uflag = 0
        pflag = 0
        c.execute('SELECT * FROM users')
        data = c.fetchall()
        for i in data:
            for j in i:
                if(j == regNO):
                    uflag = 1
                if(j == password):
                    pflag = 1
                    
            
        if((uflag == 1) and (pflag == 1)):
            print("Success")
            messagebox.showinfo("Details","Successfully Logged in")
            os.popen('py home.py')
            window1.destroy()
            
        else:
            print("Not Found")
            messagebox.showerror("Detail","Wrong Details!")




window1=Tk()
window1.geometry("1920x1080")
window1.title('LOGIN')
window1.configure(background='#E8175D')
frame_1=Frame(window1,padx="80",pady="80")
frame_1.configure(background="#212121")
label_1 = Label(window1, text="PARKING MANAGEMENT SYSTEM",fg="#CC527A",padx="642",pady="0")
label_1.configure(font=(50))
label_2=Label(frame_1,text="Reg NO : ",padx="10", bg="#212121", fg="#fff")
label_2.config(font=('algerian', 20))
Entry_1=Entry(frame_1,bd=3,width="50")
label_3=Label(frame_1,text="Password : ",padx="10", bg="#212121", fg="#fff")
label_3.config(font=('algerian', 20))
label_4=Label(frame_1,text="Login ",padx="10", bg="#212121", fg="#fff")
label_4.config(font=('algerian', 40))
Entry_2=Entry(frame_1,bd=3,width="50",show="*")
label_1.grid(row=0,column=0,sticky='nwse')
frame_1.grid(row=1,columnspan=25, pady="200")
label_2.grid(row=2,column=5)
Entry_1.grid(row=2,column=7,columnspan=5)
label_3.grid(row=4,column=5)
Entry_2.grid(row=4,column=7,columnspan=5)
label_4.grid(row=0,column=5)
button_1=Button(frame_1,text="Login",width="20",bg="#00BCD4",command=log)
button_1.grid(row=5,column=7)
button_1=Button(frame_1,text="Register",width="20",bg="#00BCD4",command=redg)
button_1.grid(row=5,column=9)              
window1.mainloop()

