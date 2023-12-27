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
class myNotice:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Notice Pannel")

        #-----------Variables-------------------
        self.var_nid=StringVar()
        self.var_ntitle=StringVar()
        self.var_ndesc=StringVar()
        self.var_datetime=StringVar()

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
        main_frame.place(x=198,y=90,width=1000,height=500)
        

        #----------------------------------------------------------------------
        right_frame = LabelFrame(main_frame,bd=2 ,relief=RIDGE,text="List of Notices",font=("verdana",12,"bold"),fg="black")
        right_frame.place(x=10,y=10,width=980,height=480)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2 ,relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="black")
        search_frame.place(x=10,y=5,width=955,height=80)

        #search
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
        table_frame.place(x=14,y=100,width=955,height=360)

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
        self.notice_table.column("ID",width=30)
        self.notice_table.column("Date Time",width=50)
        self.notice_table.column("Title",width=100)
        self.notice_table.column("Description",width=350)


        self.notice_table.pack(fill=BOTH,expand=1)
        self.notice_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ==================Function Declaration==============================
 
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
    obj=myNotice(root)
    root.mainloop()
