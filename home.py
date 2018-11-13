from tkinter import*
from tkinter import messagebox
import sqlite3
import os

root=Tk()
root.title('HOME')
root.geometry("600x500")
root.configure(background="#00C0E4")
conn =sqlite3.connect('index.db')
c = conn.cursor() 

def fun():
    os.popen('py login.py')
    root.destroy()
    
def sub():
    
    reg = e1.get()
    listoption=v.get()
    listoption1=v1.get()
    print(reg)
    print(listoption)
    print(listoption1)
    listval = (listoption,reg)
    print(listval)
    listval2 = (listoption1,reg)
    if(reg == ""):
        messagebox.showinfo("Log","Fill the Form fields Correctly")
    else:
        c.execute("UPDATE users set block=? where regNo=?",(listval))
        c.execute("UPDATE users set price=? where regNo=?",(listval2))
        messagebox.showinfo("Log","Record Updated Successfully")
        conn.commit()
        conn.close()
def sel():
    os.popen('py status.py')
    root.destroy()
    
    
    
        
l0=Label(root,text="HOME PAGE:",bg="#00C0E4",fg="#212121")
l0.config(font=('algerian', 30))
l1=Label(root,text="REG NO:",bg="#00C0E4",fg="#212121")
l1.config(font=('algerian', 15))
l2=Label(root,text="PARKING BLOCK:",bg="#00C0E4",fg="#212121")
l2.config(font=('algerian', 15))
l3=Label(root,text="PRICE:",bg="#00C0E4",fg="#212121")
l3.config(font=('algerian', 15))
e1=Entry(root,bd=1,width="50")


listoptions=('Block-1','Block-7','Block-14','Block-29','Block-34','Block-36','Block-41','Block-45','Block-55','Block-56')
v=StringVar()
v.set(listoptions[0])
c1 = OptionMenu(root,v,*listoptions )
c1.grid(row=2,column=1)
listoptions1=("Bike:Rs.5","Car:Rs.15")
v1=StringVar()
v1.set(listoptions1[0])
c2=OptionMenu(root,v1,*listoptions1)
c2.grid(row=3,column=1)

l0.grid(row=0,column=0)
l1.grid(row=1,column=0)
l2.grid(row=2,column=0)
l3.grid(row=3,column=0)

e1.grid(row=1,column=1)


B=Button(root,text="SUBMIT",bg="#212121",fg="#fff",width="10",command=sub)
B1=Button(root,text="CLOSE",bg="#212121",fg="#fff",width="10",command=fun)
B2=Button(root,text="PARKING DETAILS",bg="#212121",fg="#fff",width="15",command=sel)
B.grid(row=5,columnspan=2)
B1.grid(row=5,column=1)
B2.grid(row=5,column=0)
root.mainloop()
