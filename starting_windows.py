from tkinter import *
import os
from playsound import playsound
from PIL import Image,ImageTk
def function1():
    playsound('welcome.mp3')
    os.system("firstpage.py")
root=Tk()
root.geometry("780x660")
root.configure(bg='blue')
root.maxsize(780,660)
root.minsize(780,660)
root.update()
img=Image.open('face1.gif')
photo=ImageTk.PhotoImage(img)
label=Label(image=photo)
label.pack()
Button(root, text = 'Click Here !',height=100, width=200,bg = "green",font=("Helvetica", 32),command=function1).pack() 
root.mainloop()
