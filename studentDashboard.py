from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from time import strftime
from datetime import datetime
# --------------------------
from train import Train
from student import Student
from myattendance import MyAttendance
from face_recognition import Face_Recognition
from myNotice import myNotice
from attendance import Attendance
import os
from tkinterhtml import TkinterHtml
from chatbot import ChatBot
import subprocess


class Student_Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Dashboard")

        # backgorund image 
        bg1=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\bg0.png")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)
        #title section
        title_lb1 = Label(bg_img,bg="black",fg="white")
        title_lb1.place(x=0,y=0,width=1366,height=44)

         # College image  
        img=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\homepage.png")
        img=img.resize((1220,350),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=85,y=50,width=1220,height=350)

        #  logo  
        logo=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\logo.png")
        logo=logo.resize((130,43),Image.LANCZOS)
        self.logo=ImageTk.PhotoImage(logo)

        std_b1 = Button(title_lb1,image=self.logo,cursor="hand2",bd=0)
        std_b1.place(x=6,y=3,width=130,height=43)

        # ============================Time================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lb1, font = ('times new roman',11),background='black',foreground='white')
        lbl.place(x=1260,y=4,width=80,height=30)
        time() 

    #    buttons
         # profile
        # std_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\pr.PNG")
        # std_img_btn=std_img_btn.resize((265,125),Image.LANCZOS)
        # self.std_img1=ImageTk.PhotoImage(std_img_btn)

        # std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2",bd=1)
        # std_b1.place(x=210,y=420,width=265,height=125)

        # std_b1_1 = ttk.Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",style="Profile.TButton")
        # std_b1_1.place(x=190,y=270,width=230,height=45)

        # chatbot  button 2
        chatbot_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\c.png")
        chatbot_btn=chatbot_btn.resize((265,125),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(chatbot_btn)

        det_b1 = Button(bg_img,command=self.chatbot,image=self.det_img1,cursor="hand2",bd=1)
        det_b1.place(x=400,y=420,width=265,height=125)

        # attendance  button 3
        att_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\at.png")
        att_btn=att_btn.resize((265,125),Image.LANCZOS)
        self.det_img2=ImageTk.PhotoImage(att_btn)

        det_b2 = Button(bg_img,command=self.attendance_pannel,image=self.det_img2,cursor="hand2",bd=1)
        det_b2.place(x=790,y=420,width=265,height=125)

        # time table  button 4
        tt_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\tt.png")
        tt_btn=tt_btn.resize((265,125),Image.LANCZOS)
        self.det_img3=ImageTk.PhotoImage(tt_btn)

        det_b3 = Button(bg_img,command=self.time_stud,image=self.det_img3,cursor="hand2",bd=1)
        det_b3.place(x=400,y=560,width=265,height=125)

        # notice  button 4
        nt_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\nt.png")
        nt_btn=nt_btn.resize((265,125),Image.LANCZOS)
        self.det_img4=ImageTk.PhotoImage(nt_btn)

        det_b4 = Button(bg_img,command=self.notice,image=self.det_img4,cursor="hand2",bd=1)
        det_b4.place(x=790,y=560,width=265,height=125)
# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    # def train_pannels(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Train(self.new_window)
    
    # def face_rec(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=MyAttendance(self.new_window)

    def time_stud(self):
         subprocess.call(["python", "timetable_stud.py"])     
    
    def notice(self):
        self.new_window=Toplevel(self.root)
        self.app=myNotice(self.new_window)

    def chatbot(self):
        self.new_window = Toplevel(self.root) 
        self.app=ChatBot(self.new_window)  

    


    
    def open_img(self):
        os.startfile("dataset")

if __name__ == "__main__":
    root=Tk()
    obj=Student_Dashboard(root)
    root.mainloop()