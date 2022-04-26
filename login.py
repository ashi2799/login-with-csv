from tkinter import *
from tkinter import messagebox
import csv

def getval():
    user=userval.get()
    pass1=passval.get()
    with open("login.csv", 'rt')as file:
        csv_row = csv.reader(file)
        login=""
        for row in csv_row:
            if row[0] == user and row[1] == pass1:
                login=True
                break
            else:
                login=False

        if login==True:
            messagebox.showinfo("RESULT", "Welcome " + user)
        else:
            messagebox.showwarning("Error", "Wrong credentails")


root=Tk()
#root.geometry("644x333")

root.title("Login system")

lable=Label(text="User Login", font=100,fg="red",pady=15).grid(row=0,column=3)

userl=Label(root,text="UserName").grid(row=1,column=2)
passl=Label(root,text="password").grid(row=2,column=2)

userval=StringVar()
passval=StringVar()

userentry=Entry(root,textvariable=userval).grid(row=1,column=3)
passentry=Entry(root,textvariable=passval,show="*").grid(row=2,column=3)



Button(text="submit",command=getval).grid(row=3,column=3)



root.mainloop()

