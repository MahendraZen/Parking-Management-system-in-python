from tkinter import*
from tkinter import messagebox
import sqlite3
import os
root=Tk()
root.geometry("500x500")
conn=sqlite3.connect('index.db')
c=conn.cursor()
root.title('status')
listdet=[]
def bac():
    os.popen('py home.py')
    root.destroy()
def sta():
    if(Entry_1.get() == ""):
        messagebox.showinfo("Detail","Please fill thsi field")
    else:
        lis=[]
        print(lis)
        lis.append(Entry_1.get())
        c.execute('SELECT * FROM users WHERE regNO = ?',lis)
        res = c.fetchall()
        if(res==[]):
            messagebox.showerror("Detail Errors  ","Invalid Redg.No")
        else:
            for i in res:
                it1=i[0]
                it2=i[1]
                it3=i[4]
                it4=i[6]
                it5=i[7]
                listdet = [it1, it2, it3, it4, it5]
                print(listdet)
            indexrow0= Label(root, text="Details ")
            indexrow0.config(font=('algerian', 20))
            indexrow0.grid(row=2, column=0)
            indexrow1= Label(root, text="Name : ")
            indexrow1.grid(row=3, column=0)
            indexrow2= Label(root, text=listdet[0])
            indexrow2.grid(row=3, column=1)
            indexrow3= Label(root, text="Redg No : ")
            indexrow3.grid(row=4, column=0)
            indexrow3= Label(root, text=listdet[1])
            indexrow3.grid(row=4, column=1)
            indexrow4= Label(root, text="E-Mail : ")
            indexrow4.grid(row=5, column=0)
            indexrow5= Label(root, text=listdet[2])
            indexrow5.grid(row=5, column=1)
            indexrow6= Label(root, text="Location : ")
            indexrow6.grid(row=6, column=0)
            indexrow7= Label(root, text=listdet[3])
            indexrow7.grid(row=6, column=1)
            indexrow8= Label(root, text="Catogery : ")
            indexrow8.grid(row=7, column=0)
            indexrow9= Label(root, text=listdet[4])
            indexrow9.grid(row=7, column=1)

        

label=Label(root,text="REG NO")
label.config(font=('algerian', 20))
Entry_1=Entry(root,bd=2,width="20")
bu = Button(root, text="Submit", command=sta,width="10")
bu1 = Button(root, text="Back", command=bac,width="10")
label.grid(row=0,column=0)
Entry_1.grid(row=0,column=1)
bu.grid(row=1, column=0)
bu1.grid(row=1, column=1)


root.mainloop()
