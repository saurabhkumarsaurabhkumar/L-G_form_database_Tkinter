from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk #pip install pillow
import pymysql #pip install pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry('1350x700+0+0')

        self.root.config(bg="white")
        ## ================Bg Image======
        self.bg=ImageTk.PhotoImage(file="images/background1.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        ##============Left Image=====
        self.left=ImageTk.PhotoImage(file="images/2.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        ##=========Register Frame============
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=230,y=30)
        ###First Name
        f_name=Label(frame1,text="First Name*",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)


        ##Last Name
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        ##Contact Number
        contact=Label(frame1,text="Contact No.*",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        ## Email
        email=Label(frame1,text="Email*",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        ## Combobox====Security Question
        Qustion=Label(frame1,text="Choose Branch*",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_question=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)

        self.cmb_question['values']=('Select','CSE','EEE','CIVIL','MECHENICAL','EI')
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)
        ## ====Security Answer
        reg_no=Label(frame1,text="Registration No.*",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_regno=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_regno.place(x=370,y=270,width=250)

        ##Password
        Password=Label(frame1,text="Password *",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_pass=Entry(frame1,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_pass.place(x=50,y=350,width=250)

        ##Confirm Password
        Cpassword=Label(frame1,text="Confirm Password *",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpass=Entry(frame1,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_cpass.place(x=370,y=350,width=250)
        ##========Term and Condition

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The  Terms & Condition *",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

        ###=======Register Button=========
        # self.btn_img=ImageTk.PhotoImage(file="images/regbtn2.jpg")
        btn=Button(frame1,text="Sign Up",font=("times new roman",15,"bold"),bg="white",fg="green",bd=0,cursor="hand2",command=self.register_data).place(x=200,y=420,width=160,height=50)

        btn=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",15,"bold"),bg="white",fg="green",bd=0,cursor="hand2").place(x=200,y=510,width=160,height=50)


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)

        self.cmb_question.current(0)
        self.txt_regno.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_cpass.delete(0,END)


    def login_window(self):
        self.root.destroy()
        import login

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="" or self.txt_regno.get()=="" or self.txt_pass.get()=="" or self.txt_cpass.get()=="" :
            messagebox.showerror("Error","All Fields Are Required, Please Check it",parent=self.root)
        elif self.txt_pass.get()!=self.txt_cpass.get():
            messagebox.showerror("Error","Password & Confirm Password Should be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & Condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                cur=con.cursor()
                cur.execute("select * from employee where Regitration=%s",self.txt_regno.get())
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","This registration number already exist,Please try another registration number",parent=self.root)
                else:

                    cur.execute("insert into employee (First_Name,Last_Name,Contact,Email,Branch,Regitration,Password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.txt_fname.get(),
                                        self.txt_lname.get(),
                                        self.txt_contact.get(),
                                        self.txt_email.get(),
                                        self.cmb_question.get(),
                                        self.txt_regno.get(),
                                        self.txt_pass.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Sucess","Register Successfully",parent=self.root)
                    self.clear()
                    self.root.destroy()
                    import login

            except Exception as es:
                messagebox.showinfo("Error",f"Error Due to :{str(es)}",parent=self.root)

            


root=Tk()
obj=Register(root)
root.mainloop()