from tkinter import *
import os
root=Tk()
root.geometry("800x520")
root.maxsize(800,520)
root.minsize(800,520)
root.configure(bg='#5e082e')
def function1():
    os.startfile("D:\FINAL PROJECT\Calculator App\calculator.py")
def function7():
    root.destroy()
def function2():
    os.startfile("firstpage.py")
    root.destroy()
w = Label(root, text="  STUDENT STUDY PURPOSE ", bg="#5e082e", fg="white",font=("Georgia", 32)).grid(padx=35,pady=15)
Button(root,text="CALCULATOR",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=2,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)
Button(root,text="ZIP FILE EXTRACTOR",font=("times new roman",20),bg="#0D47A1",fg='white').grid(row=3,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)
Button(root,text="NOTEPAD",font=("times new roman",20),bg="#0D47A1",fg='white').grid(row=4,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)
Button(root,text="<= BACK",font=("times new roman",20),bg="#2f065e",fg='white',command=function2).grid(row=5,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)
Button(root,text="EXIT =>",font=("times new roman",20),bg="red",fg='white',command=function7).grid(row=6,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)


root.mainloop()
