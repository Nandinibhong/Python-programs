from tkinter import*
parent=Tk()
name=Label(parent,text="Name").grid(row=0,column=0)
e1=Entry(parent).grid(row=0,column=1)
password=Label(parent,text="Password").grid(row=1,column=0)
e2=Entry(parent).grid(row=1,column=1)
submit=Button(parent,text="submit").grid(row=4,column=0)
parent.mainloop()