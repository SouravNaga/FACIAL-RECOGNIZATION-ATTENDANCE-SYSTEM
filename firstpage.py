from tkinter import *
import os
from PIL import Image,ImageTk
root1=Tk()
root1.update()
def function1():
    os.system('use_webcam.py')
def function2():
    os.system('train1.py')
def function3():
    os.system('train2.py')
def function4():
    os.system('read_excel.py')
def function5():
    root1.destroy()
    os.system('function5.py')
def function6():
    os.startfile("D:\FINAL PROJECT\souravProj\index.html")
def function7():
    root1.destroy()
root1.geometry("850x670")
root1.configure(bg='#150227')
root1.maxsize(850,670)
root1.minsize(850,670)
w = Label(root1, text="   FACIAL  ATTENDANCE  SYSTEM ", bg="#150227", fg="white",font=("Georgia", 32)).grid(padx=35)
Button(root1,text="Create Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=2,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)
Button(root1,text="Train Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)
Button(root1,text="Recognize + Attendance",font=("times new roman",20),bg="#0D47A1",fg='white',command=function3).grid(row=4,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)
Button(root1,text="Open DataSheet",font=("times new roman",20),bg="#0D47A1",fg='white',command=function4).grid(row=5,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)
Button(root1,text="Student Study Purpose",font=("times new roman",20),bg="#0D47A1",fg='white',command=function5).grid(row=6,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)
Button(root1,text="Details About Developer & Project",font=("times new roman",20),bg="#900775",fg='white',command=function6).grid(row=7,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)
Button(root1,text="EXIT",font=("times new roman",20),bg="red",fg='white',command=function7).grid(row=8,columnspan=2,sticky=W+E+N+S,padx=35,pady=15)
root1.mainloop()
