from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install pillow
import pymysql #pip install pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Home")
        self.root.geometry('1350x700+0+0')
        self.root.config(bg="green")
        title=Label(self.root,text="WELCOME",font=("times new roman",45,"bold"),bg="green",fg="yellow").place(x=590,y=30)






root=Tk()
obj=Register(root)
root.mainloop()