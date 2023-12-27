from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
import os
# Testing Connection 
"""
conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
"""
class Notice:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Notice Pannel")

        #-----------Variables-------------------
        self.var_nid=StringVar()
        self.var_ntitle=StringVar()
        self.var_ndesc=StringVar()
        self.var_datetime=StringVar()
        # self.var_semester=StringVar()
        # self.var_std_id=StringVar()
        # self.var_std_name=StringVar()
        # self.var_div=StringVar()
        # self.var_roll=StringVar()
        # self.var_gender=StringVar()
        # self.var_dob=StringVar()
        # self.var_email=StringVar()
        # self.var_mob=StringVar()
        # self.var_address=StringVar()
        # self.var_teacher=StringVar()

    # This part is image labels setting start 
        # first header image  
        # img=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\banner.jpg")
        # img=img.resize((1366,130),Image.LANCZOS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # # set image as lable
        # f_lb1 = Label(self.root,image=self.photoimg)
        # f_lb1.place(x=0,y=0,width=1366,height=130)

         # backgorund image 
        bg1=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\backg.png")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img)
        title_lb1.place(x=0,y=0,width=1366,height=45)

        #  logo  
        logo=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\lg.png")
        logo=logo.resize((130,43),Image.LANCZOS)
        self.logo=ImageTk.PhotoImage(logo)

        std_b1 = Button(title_lb1,image=self.logo,cursor="hand2",bd=0)
        std_b1.place(x=6,y=2,width=130,height=43)


            # ============================Time================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lb1, font = ('times new roman',11),foreground='black')
        lbl.place(x=1260,y=4,width=80,height=30)
        time()    

        # Creating Frame 
        main_frame = Frame(bg_img,bd=0) #bd mean border 
        main_frame.place(x=4,y=99,width=1355,height=480)
        

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Notice",font=("verdana",12,"bold"),fg="black")
        left_frame.place(x=10,y=10,width=660,height=500)

        #Class Student Information
        class_Student_frame = LabelFrame(left_frame,bd=2 ,relief=RIDGE,text="Add Notice",font=("verdana",12,"bold"),fg="black")
        class_Student_frame.place(x=10,y=12,width=635,height=230)


        #Notice title
        student_name_label = Label(class_Student_frame,text="Notice title:",font=("verdana",12,"bold"),fg="black" )
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_ntitle,width=37,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #desc
        desc = Label(class_Student_frame,text="Notice Description:",font=("verdana",12,"bold"),fg="black" )
        desc.grid(row=2,column=2,padx=5,pady=10,sticky=W)

        desc_entry = ttk.Entry(class_Student_frame,textvariable=self.var_ndesc,width=37,font=("verdana",12,"bold"))
        desc_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

         #date ime
        ndate = Label(class_Student_frame,text="Notice Date:",font=("verdana",12,"bold"),fg="black" )
        ndate.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        ndate_entry = ttk.Entry(class_Student_frame,textvariable=self.var_datetime,width=37,font=("verdana",12,"bold"))
        ndate_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

          #date ime
        nid = Label(class_Student_frame,text="Notice ID:",font=("verdana",12,"bold"),fg="black" )
        nid.grid(row=6,column=2,padx=5,pady=5,sticky=W)

        nid_entry = ttk.Entry(class_Student_frame,textvariable=self.var_nid,width=37,font=("verdana",12,"bold"))
        nid_entry.grid(row=6,column=3,padx=5,pady=5,sticky=W)


        #Button Frame
        btn_frame = Frame(left_frame,bd=2 ,relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        #save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=7,font=("verdana",12,"bold"),fg="white",bg="green")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=7,font=("verdana",12,"bold"),fg="white",bg="black")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #delete button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=7,font=("verdana",12,"bold"),fg="white",bg="red")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=7,font=("verdana",12,"bold"),fg="white",bg="orange")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)


        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2 ,relief=RIDGE,text="List of Notices",font=("verdana",12,"bold"),fg="black")
        right_frame.place(x=680,y=10,width=660,height=480)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2 ,relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="black")
        search_frame.place(x=10,y=5,width=635,height=80)

        #Phone Number
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="black" )
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","nid")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="blue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="darkblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2 ,relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.notice_table = ttk.Treeview(table_frame,column=("ID","Title","Description","Date Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.notice_table.xview)
        scroll_y.config(command=self.notice_table.yview)

        self.notice_table.heading("ID",text="ID")
        self.notice_table.heading("Date Time",text="Date Time")
        self.notice_table.heading("Title",text="Title")
        self.notice_table.heading("Description",text="Description")
        self.notice_table["show"]="headings"


        # Set Width of Colums 
        self.notice_table.column("ID",width=100)
        self.notice_table.column("Date Time",width=100)
        self.notice_table.column("Title",width=100)
        self.notice_table.column("Description",width=100)
        # self.notice_table.column("Course",width=100)
        # self.notice_table.column("Year",width=100)
        # self.notice_table.column("Sem",width=100)
        # self.notice_table.column("Div",width=100)
        # self.notice_table.column("Gender",width=100)
        # self.notice_table.column("DOB",width=100)
        # self.notice_table.column("Mob-No",width=100)
        # self.notice_table.column("Address",width=100)
        # self.notice_table.column("Roll-No",width=100)
        # self.notice_table.column("Email",width=100)
        # self.notice_table.column("Teacher",width=100)
        # self.notice_table.column("Photo",width=100)


        self.notice_table.pack(fill=BOTH,expand=1)
        self.notice_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ==================Function Declaration==============================
    def add_data(self):
        if self.var_ntitle.get=="" or self.var_ndesc.get()=="" or self.var_nid.get()=="" or self.var_datetime.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into notes values(%s,%s,%s,%s)",(
                # self.var_ntitle.get(),
                # self.var_ndesc.get(),
                # self.var_datetime.get(),
                # self.var_nid.get(),
                self.var_nid.get(),
                self.var_ntitle.get(),
                self.var_ndesc.get(),
                self.var_datetime.get(),
                # self.var_div.get(),
                # self.var_gender.get(),
                # self.var_dob.get(),
                # self.var_mob.get(),
                # self.var_address.get(),
                # self.var_roll.get(),
                # self.var_email.get(),
                # self.var_teacher.get(),
                # self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from notes")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.notice_table.delete(*self.notice_table.get_children())
            for i in data:
                self.notice_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.notice_table.focus()
        content = self.notice_table.item(cursor_focus)
        data = content["values"]

        self.var_ntitle.set(data[1]),
        self.var_ndesc.set(data[2]),
        self.var_datetime.set(data[3]),
        self.var_nid.set(data[0]),
        # self.var_year.set(data[4]),
        # self.var_semester.set(data[5]),
        # self.var_div.set(data[6]),
        # self.var_gender.set(data[7]),
        # self.var_dob.set(data[8]),
        # self.var_mob.set(data[9]),
        # self.var_address.set(data[10]),
        # self.var_roll.set(data[11]),
        # self.var_email.set(data[12]),
        # self.var_teacher.set(data[13]),
        # self.var_radio1.set(data[14])
    # ========================================Update Function==========================
    def update_data(self):
        if self.var_nid.get()=="" or self.var_ntitle=="" or self.var_ndesc.get()=="" or self.var_datetime.get()=="" :
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Notice Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update notes set nid=%s,ntitle=%s,ndesc=%s,datetime=%s",( 
                    self.var_nid.get(),
                    self.var_ntitle.get(),
                    self.var_ndesc.get(),
                    self.var_datetime.get()   
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_nid.get()=="":
            messagebox.showerror("Error","Notice Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from notes where nid=%s"
                    val=(self.var_nid.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Reset Function 
    def reset_data(self):
        self.var_nid.set(""),
        self.var_ntitle.set(""),
        self.var_ndesc.set(""),
        self.var_datetime.set(""),
    
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT ntitle,ndesc,datetime FROM notes where nid='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.notice_table.delete(*self.notice_table.get_children())
                    for i in rows:
                        self.notice_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Notice(root)
    root.mainloop()
