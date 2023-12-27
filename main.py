from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from time import strftime
from datetime import datetime
import os
from tkinterhtml import TkinterHtml
from chatbot import ChatBot  
from timetable_dash import TimeTable_Dashboard
from notice import Notice
# from tkinter.scrolledtext import ScrolledText
# from timetable_stud import Timetable
import subprocess
# from login import Login

class Face_Recognition_System:
    def __init__(self,root):
            self.root=root
            self.root.geometry("7366x778+0+0")
            self.root.title("Intelligent College Manager")

            # This part is image labels setting start 
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

            # Create buttons below the section 
            # ------------------------------------------------------------------------------------------------------------------- 
            # student button 1
            std_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\st.png")
            std_img_btn=std_img_btn.resize((265,125),Image.LANCZOS)
            self.std_img1=ImageTk.PhotoImage(std_img_btn)

            std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2",bd=0)
            std_b1.place(x=100,y=410,width=265,height=125)

            # std_b1_1 = ttk.Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",style="Profile.TButton")
            # std_b1_1.place(x=190,y=270,width=230,height=45)

            # Detect Face  button 2
            det_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\fr.png")
            det_img_btn=det_img_btn.resize((265,125),Image.LANCZOS)
            self.det_img1=ImageTk.PhotoImage(det_img_btn)

            det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",bd=0)
            det_b1.place(x=400,y=410,width=265,height=125)

            # det_b1_1 = ttk.Button(bg_img,command=self.face_rec,text="Face Recognition",cursor="hand2",style="Profile.TButton")
            # det_b1_1.place(x=460,y=270,width=230,height=45)

            # Attendance System  button 3
            att_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\at.PNG")
            att_img_btn=att_img_btn.resize((265,125),Image.LANCZOS)
            self.att_img1=ImageTk.PhotoImage(att_img_btn)

            att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",bd=0)
            att_b1.place(x=700,y=410,width=265,height=125)

            # att_b1_1 = ttk.Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",style="Profile.TButton")
            # att_b1_1.place(x=720,y=270,width=230,height=45)

            #  Notice  button 4
            hlp_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\nt.png")
            hlp_img_btn=hlp_img_btn.resize((265,125),Image.LANCZOS)
            self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

            hlp_b1 = Button(bg_img,image=self.hlp_img1,command=self.notice,cursor="hand2",bd=0)
            hlp_b1.place(x=1000,y=410,width=265,height=125)

            # hlp_b1_1 = ttk.Button(bg_img,text="Fees Status",command=self.helpSupport,cursor="hand2",style="Profile.TButton")
            # hlp_b1_1.place(x=990,y=270,width=230,height=45)

            # Top 4 buttons end.......
            # ---------------------------------------------------------------------------------------------------------------------------
            # Start below buttons.........
            #  Train   button 5
            tra_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\ti.png")
            tra_img_btn=tra_img_btn.resize((265,125),Image.LANCZOS)
            self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

            tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",bd=0)
            tra_b1.place(x=100,y=548,width=265,height=125)

            # tra_b1_1 = ttk.Button(bg_img,command=self.train_pannels,text="Training Data",cursor="hand2",style="Profile.TButton")
            # tra_b1_1.place(x=190,y=520,width=230,height=45)

            # timetable   button 6
            pho_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\tt.png")
            pho_img_btn=pho_img_btn.resize((265,125),Image.LANCZOS)
            self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

            pho_b1 = Button(bg_img,command=self.timetable,image=self.pho_img1,cursor="hand2",bd=0)
            pho_b1.place(x=400,y=548,width=265,height=125)
            
            # chatbot button 7
            dev_img_btn = Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\c.png")
            dev_img_btn = dev_img_btn.resize((265,125), Image.LANCZOS)
            self.dev_img1 = ImageTk.PhotoImage(dev_img_btn)

            dev_b1 = Button(bg_img, command=self.chatbot, image=self.dev_img1, cursor="hand2",bd=0)
            dev_b1.place(x=700, y=548, width=265, height=125)
        
            # teacher   button 8
            exi_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\teacher.png")
            exi_img_btn=exi_img_btn.resize((265,125),Image.LANCZOS)
            self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

            exi_b1 = Button(bg_img, command=self.teacher,image=self.exi_img1,cursor="hand2",bd=0)
            exi_b1.place(x=1000,y=548,width=265,height=125)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("dataset")

    def iExit(self):
        self.iExit=ttk.messagebox.askyesno("Face Recogition","Are you sure you  want to exit?",parent=self.root) 
        if self.iExit>0:
            exit.root.destroy()  
        else:
            return     
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    
    # def run_program(self):
    #      subprocess.call(["python", "timetable_fac.py"])    

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def timetable(self):
        self.new_window=Toplevel(self.root)
        self.app=TimeTable_Dashboard(self.new_window)     
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def teacher(self):
         subprocess.call(["python", "teacher.py"])  

    def chatbot(self):
        self.new_window = Toplevel(self.root) 
        self.app=ChatBot(self.new_window)  

    def notice(self):
        self.new_window = Toplevel(self.root) 
        self.app=Notice(self.new_window)      

    # def logout(n):
    #     f8=Frame(bg="pink")
    #     f8.pack()
    #     n.add(f8,text="Logout")    

    def Close(self):
        root.destroy()



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
