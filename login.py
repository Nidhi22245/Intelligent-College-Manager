from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
# --------------------------
from train import Train
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os
from tkinterhtml import TkinterHtml
from main import Face_Recognition_System as fr
from teacher_dash import Teacher_dash as tr
from studentDashboard import Student_Dashboard as sd


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        # # window transparency
        # self.root.attributes("-alpha", 0.9)
        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        # self.bg=ImageTk.PhotoImage(file=r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\loginBg1.jpg")
          # backgorund image 
        bg=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\backg.png")
        bg=bg.resize((1364,766),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)

        # lb1_bg=Label(self.root,image=self.bg)
        # lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="white")
        frame1.place(x=500,y=160,width=340,height=450)

        img1=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\lg.png")
        img1=img1.resize((138,92),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1 )
        lb1img1.place(x=610,y=180, width=138,height=92)

        # get_str = Label(frame1,text="Sign In",font=("times new roman",20,"bold"),fg="brown")
        # get_str.place(x=140,y=110)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="brown",bg="white")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="brown",bg="white" )
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"),show="*")
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Sign In",font=("times new roman",15,"bold"),bg="white",bd=2,relief=RIDGE,fg="brown" ,activeforeground="white",activebackground="purple")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Sign Up",font=("times new roman",10,"bold"),bg="white",bd=0,relief=RIDGE,fg="brown" ,activeforeground="white",activebackground="purple")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bg="white",bd=0,relief=RIDGE,fg="brown" ,activeforeground="white",activebackground="purple")
        loginbtn.place(x=90,y=370,width=50,height=20)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="123"):
                open_min=messagebox.askyesno("YesNo","Are you Accessing as Admin ?")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=fr(self.new_window)
                else:
                    if not open_min:
                        # student portal here
                        return
        elif(self.txtuser.get()=="meghna bapat" and self.txtpwd.get()=="123"):
                open_min=messagebox.askyesno("YesNo","Are you Accessing as Teacher ?")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=tr(self.new_window)
                else:
                    if not open_min:
                        # student portal here
                        return            
        
                   
                    # messagebox.showinfo("Sussessful!! ","Welcome Admin to Intelligent College Manager- Admin")
                    # self.new_window=Toplevel(self.root)
                    # self.app=Face_Recognition_System(self.new_window)
                
                    # ==============================================================
            # messagebox.showinfo("Sussessfully","Welcome to Intelligent College Manager")
        else:
            # =======================================================
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from student where email=%s and DOB=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                    messagebox.showinfo("Sussessful","Welcome to Intelligent College Manager - Student")
                    self.new_window=Toplevel(self.root)
                    self.app=sd(self.new_window)
                
            # ==============================================================
            # messagebox.showerror("Error","Please Check Username or Password !")
            # conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
            # mycursor = conn.cursor()
            # mycursor.execute("select * from regteach where email=%s and pwd=%s",(
            #     self.txtuser.get(),
            #     self.txtpwd.get()
            # ))
            # row=mycursor.fetchone()
            # if row==None:
            #     messagebox.showerror("Error","Invalid Username and Password!")
            # else:
            #     open_min=messagebox.askyesno("YesNo","Are you Accessing as Admin ?")
            #     if open_min>0:
            #         self.new_window=Toplevel(self.root)
            #         self.app=Face_Recognition_System(self.new_window)
            #     else:
            #         if not open_min:
            #             # student portal here
            #             return
        
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)


            

# =====================main program Face deteion system====================
class Face_Recognition_System:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1366x768+0+0")
#         self.root.title("Face_Recogonition_System")

# # This part is image labels setting start 
#         # first header image  
#         # img=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\banner.jpg")
#         # img=img.resize((1,1),Image.LANCZOS)
#         # self.photoimg=ImageTk.PhotoImage(img)

#         # set image as lable
#         # f_lb1 = Label(self.root,image=self.photoimg)
#         # f_lb1.place(x=0,y=0,width=1366,height=130)

#         # backgorund image 
#         bg1=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\bg0.jpg")
#         bg1=bg1.resize((1366,768),Image.LANCZOS)
#         self.photobg1=ImageTk.PhotoImage(bg1)

#         # set image as lable
#         bg_img = Label(self.root,image=self.photobg1)
#         bg_img.place(x=0,y=0,width=1366,height=768)


#         #title section
#         title_lb1 = Label(bg_img,text="Intelligent College Manager",font=("verdana",30,"bold") ,fg="brown")
#         title_lb1.place(x=0,y=0,width=1366,height=45)

#         # Create buttons below the section 
#         # ------------------------------------------------------------------------------------------------------------------- 
#         # student button 1
#         std_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\std1.jpg")
#         std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
#         self.std_img1=ImageTk.PhotoImage(std_img_btn)

#         std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
#         std_b1.place(x=250,y=100,width=180,height=180)

#         std_b1_1 = ttk.Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",style="Profile.TButton")
#         std_b1_1.place(x=250,y=280,width=180,height=45)

#         # Detect Face  button 2
#         det_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\det1.jpg")
#         det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
#         self.det_img1=ImageTk.PhotoImage(det_img_btn)

#         det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
#         det_b1.place(x=480,y=100,width=180,height=180)

#         det_b1_1 = ttk.Button(bg_img,command=self.face_rec,text="Face Recognition",cursor="hand2",style="Profile.TButton")
#         det_b1_1.place(x=480,y=280,width=180,height=45)

#          # Attendance System  button 3
#         att_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\att.jpg")
#         att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
#         self.att_img1=ImageTk.PhotoImage(att_img_btn)

#         att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
#         att_b1.place(x=710,y=100,width=180,height=180)

#         att_b1_1 = ttk.Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",style="Profile.TButton")
#         att_b1_1.place(x=710,y=280,width=180,height=45)

#         #  Help  Support  button 4
#         hlp_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\hlp.jpg")
#         hlp_img_btn=hlp_img_btn.resize((180,180),Image.LANCZOS)
#         self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

#         hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",)
#         hlp_b1.place(x=940,y=100,width=180,height=180)

#         hlp_b1_1 = ttk.Button(bg_img,text="Fees Status",cursor="hand2",style="Profile.TButton")
#         hlp_b1_1.place(x=940,y=280,width=180,height=45)

#         # Top 4 buttons end.......
#         # ---------------------------------------------------------------------------------------------------------------------------
#         # Start below buttons.........
#         #  Train   button 5
#         tra_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\tra1.jpg")
#         tra_img_btn=tra_img_btn.resize((180,180),Image.LANCZOS)
#         self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

#         tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
#         tra_b1.place(x=250,y=350,width=180,height=180)

#         tra_b1_1 = ttk.Button(bg_img,command=self.train_pannels,text="Training Data",cursor="hand2",style="Profile.TButton")
#         tra_b1_1.place(x=250,y=530,width=180,height=45)

#         # Photo   button 6
#         pho_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\qr1.jpg")
#         pho_img_btn=pho_img_btn.resize((180,180),Image.LANCZOS)
#         self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

#         pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",)
#         pho_b1.place(x=480,y=350,width=180,height=180)

#         pho_b1_1 = ttk.Button(bg_img,command=self.open_img,text="Payment",cursor="hand2",style="Profile.TButton")
#         pho_b1_1.place(x=480,y=530,width=180,height=45)

#         # Developers   button 7
#         # dev_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\dev.jpg")
#         # dev_img_btn=dev_img_btn.resize((180,180),Image.LANCZOS)
#         # self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

#         # dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2",)
#         # dev_b1.place(x=710,y=350,width=180,height=180)

#         # dev_b1_1 = Button(bg_img,command=self.developr,text="Profile",cursor="hand2",font=("tahoma",15,"bold") ,fg="lightblue")
#         # dev_b1_1.place(x=710,y=530,width=180,height=45)

#         # start =====================================================================
#         # style = ttk.Style()
#         # style.configure("NoBorder.TButton", font=("tahoma", 15, "bold"), foreground="white", background="#002B53", borderwidth=0)
#         # style.map("NoBorder.TButton",
#         #     foreground=[("active", "blue")],
#         #     background=[("active", "white")])
        
#         # Developers button 7
#         dev_img_btn = Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\dev.jpg")
#         dev_img_btn = dev_img_btn.resize((180, 180), Image.LANCZOS)
#         self.dev_img1 = ImageTk.PhotoImage(dev_img_btn)

#         dev_b1 = Button(bg_img, command=self.developr, image=self.dev_img1, cursor="hand2")
#         dev_b1.place(x=710, y=350, width=180, height=180)

#         # Create a custom style for the button
#         style = ttk.Style()
#         style.configure("Profile.TButton", font=("tahoma", 15, "bold"), foreground="purple", background="white",borderwidth=0)
#         style.map("Profile.TButton",
#                 foreground=[("active", "blue")],
#                 background=[("active", "white")])

#         dev_b1_1 = ttk.Button(bg_img, command=self.developr, text="Profile", cursor="hand2", style="Profile.TButton")
#         dev_b1_1.place(x=710, y=530, width=180, height=45)
#         # end  ==========================================================================
       
#         # exit   button 8
#         exi_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\exi.jpg")
#         exi_img_btn=exi_img_btn.resize((180,180),Image.LANCZOS)
#         self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

#         exi_b1 = Button(bg_img,image=self.exi_img1,cursor="hand2",)
#         exi_b1.place(x=940,y=350,width=180,height=180)

#         exi_b1_1 = ttk.Button(bg_img,text="Exit/Notification",cursor="hand2",style="Profile.TButton")
#         exi_b1_1.place(x=940,y=530,width=180,height=45)

      


# ==================Funtion for Open Images Folder==================
#     def open_img(self):
#         os.startfile("data_img")
# # ==================Functions Buttons=====================
#     def student_pannels(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Student(self.new_window)

#     def train_pannels(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Train(self.new_window)
    
#     def face_rec(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Face_Recognition(self.new_window)
    
#     def attendance_pannel(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Attendance(self.new_window)
    
#     def developr(self):
#         self.new_window=Toplevel(self.root)
#         self.app=Developer(self.new_window) 
    
#     def open_img(self):
#         os.startfile("dataset")
    
  
# class Student_Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Dashboard")

        # backgorund image 
        bg1=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\bg0.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Intelligent College Manager",font=("verdana",30,"bold") ,fg="brown")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        # std_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\std1.jpg")
        # std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        # self.std_img1=ImageTk.PhotoImage(std_img_btn)

        # std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        # std_b1.place(x=250,y=100,width=180,height=180)

        # std_b1_1 = ttk.Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",style="Profile.TButton")
        # std_b1_1.place(x=250,y=280,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=390,y=100,width=180,height=180)

        det_b1_1 = ttk.Button(bg_img,command=self.face_rec,text="ChatBot",cursor="hand2",style="Profile.TButton")
        det_b1_1.place(x=390,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=640,y=100,width=180,height=180)

        att_b1_1 = ttk.Button(bg_img,command=self.attendance_pannel,text=" My Attendance",cursor="hand2",style="Profile.TButton")
        att_b1_1.place(x=640,y=280,width=180,height=45)

        #  Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\hlp.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=900,y=100,width=180,height=180)

        hlp_b1_1 = ttk.Button(bg_img,text="Fees Status",cursor="hand2",style="Profile.TButton")
        hlp_b1_1.place(x=900,y=280,width=180,height=45)

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
        # #  Train   button 5
        # tra_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\tra1.jpg")
        # tra_img_btn=tra_img_btn.resize((180,180),Image.LANCZOS)
        # self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        # tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        # tra_b1.place(x=250,y=350,width=180,height=180)

        # tra_b1_1 = ttk.Button(bg_img,command=self.train_pannels,text="Training Data",cursor="hand2",style="Profile.TButton")
        # tra_b1_1.place(x=250,y=530,width=180,height=45)

        # Photo   button 6
        pho_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\qr1.jpg")
        pho_img_btn=pho_img_btn.resize((180,180),Image.LANCZOS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=390,y=350,width=180,height=180)

        pho_b1_1 = ttk.Button(bg_img,command=self.open_img,text="Payment",cursor="hand2",style="Profile.TButton")
        pho_b1_1.place(x=390,y=530,width=180,height=45)

        # Developers   button 7
        # dev_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\dev.jpg")
        # dev_img_btn=dev_img_btn.resize((180,180),Image.LANCZOS)
        # self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        # dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2",)
        # dev_b1.place(x=710,y=350,width=180,height=180)

        # dev_b1_1 = Button(bg_img,command=self.developr,text="Profile",cursor="hand2",font=("tahoma",15,"bold") ,fg="lightblue")
        # dev_b1_1.place(x=710,y=530,width=180,height=45)

        # start =====================================================================
        # style = ttk.Style()
        # style.configure("NoBorder.TButton", font=("tahoma", 15, "bold"), foreground="white", background="#002B53", borderwidth=0)
        # style.map("NoBorder.TButton",
        #     foreground=[("active", "blue")],
        #     background=[("active", "white")])
        
        # Developers button 7
        dev_img_btn = Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\dev.jpg")
        dev_img_btn = dev_img_btn.resize((180, 180), Image.LANCZOS)
        self.dev_img1 = ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img, command=self.developr, image=self.dev_img1, cursor="hand2")
        dev_b1.place(x=640, y=350, width=180, height=180)

        # Create a custom style for the button
        style = ttk.Style()
        style.configure("Profile.TButton", font=("tahoma", 15, "bold"), foreground="purple", background="white",borderwidth=0)
        style.map("Profile.TButton",
                foreground=[("active", "blue")],
                background=[("active", "white")])

        dev_b1_1 = ttk.Button(bg_img, command=self.developr, text="Profile", cursor="hand2", style="Profile.TButton")
        dev_b1_1.place(x=640, y=530, width=180, height=45)
        # end  ==========================================================================
       
        # exit   button 8
        exi_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\exi.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.LANCZOS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=900,y=350,width=180,height=180)

        exi_b1_1 = ttk.Button(bg_img,text="Exit/Notification",cursor="hand2",style="Profile.TButton")
        exi_b1_1.place(x=900,y=530,width=180,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    
    def open_img(self):
        os.startfile("dataset")

# ==================Funtion for Open Images Folder==================
def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    
def open_img(self):
        os.startfile("dataset")


if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()