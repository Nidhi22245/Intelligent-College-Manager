from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
  
class ChatBot:
    def __init__(self,root):
        self.root = root
        self.root.title('ChatBot')
        self.root.geometry('730x620+0+0')
        self.root.bind('<Return>',self.enter_func)

        main_frame = Frame(self.root,bd=3,bg='brown',width = 620)
        main_frame.pack()

        img_chat = Image.open("Images_GUI\chat.jpg")
        img_chat = img_chat.resize((200,70),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame,bd=3,relief = RAISED,anchor = 'nw', width=740,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='purple',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y = ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text = Text(main_frame,width=65,heigh=20,bd=3 ,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side = RIGHT,fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root,bd=4,bg='white',width = 730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Chat Here",font=('arial',14,'bold'),fg='purple',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',14,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',14,'bold'),width=8,bg='purple')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',14,'bold'),width=8,bg='purple')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg = ''
        self.label_2=Label(btn_frame,text=self.msg,font=('times new roman',14,'bold'),fg='purple',bg='white')
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)

    # =================================  Function ------------------------------
    
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')  

 
    def send(self):
        send = '\t\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if(self.entry.get()==''):
            self.msg = 'Please Enter Some Input'
            self.label_2.config(text=self.msg,fg = 'red')
        elif (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi! How can I assist you today?')
        elif (self.entry.get()=='who created you?'):
            self.text.insert(END,'\n\n'+'Bot: I was created by developer Nidhi in Python.')
        elif (self.entry.get()=='what is your name?'):
            self.text.insert(END,'\n\n'+'Bot: My name is Bot, and What\'s your\'s?')          
        elif (self.entry.get()=='what do you do?'):
            self.text.insert(END,'\n\n'+'Bot:  I am an intelligent college manager designed to provide information about courses, schedules, and other college-related details. How can I assist you today?')     
        elif (self.entry.get()=='Can you provide me with my attendance report?'):
            self.text.insert(END,'\n\n'+'Bot: Sure, please provide me with your student ID.') 
        elif (self.entry.get()=='How do I pay my tuition fees?'):
            self.text.insert(END,'\n\n'+'Bot:  You can pay your tuition fees online through our payment portal. Would you like instructions?')
        elif (self.entry.get()==' What\'s the deadline for paying my fees?'):
            self.text.insert(END,'\n\n'+'Bot: The deadline for fee payment is [deadline date]. Make sure to pay before that to avoid any late fees.')  
        elif (self.entry.get()=='Tell me about the upcoming college events.'):
            self.text.insert(END,'\n\n'+'Bot:  We have several exciting events coming up, including [event names]. Would you like more details?')  
        elif (self.entry.get()=='How can I reset my college email password?'):
            self.text.insert(END,'\n\n'+'Bot: You can reset your password by visiting our college email portal and following the \'Forgot Password\' link.') 
        elif (self.entry.get()=='Can you help me with the course registration process?'):
            self.text.insert(END,'\n\n'+'Bot:  Certainly! Course registration typically starts [registration start date]. Would you like a step-by-step guide?')
        elif (self.entry.get()=='Can I change my major?'):
            self.text.insert(END,'\n\n'+'Bot: Yes, you can change your major by contacting the academic advising office. They will guide you through the process.')
        elif (self.entry.get()==' What is the procedure for getting a student ID card?'):
            self.text.insert(END,'\n\n'+'Bot:  You can obtain a student ID card at the registration office. Please bring a valid photo ID and proof of enrollment.')  
        elif (self.entry.get()=='Tell me more about the face recognition attendance system.'):
            self.text.insert(END,'\n\n'+'Bot:  Our face recognition attendance system is a convenient way to mark your attendance using facial recognition technology. It ensures accurate attendance records.') 
        elif (self.entry.get()=='Bye'):
            self.text.insert(END,'\n\n'+'Bot: Thankyou for Chatting.')
        else:
            self.text.insert(END,'\n\nBot: Sorry I didn\'t get it.')
            # self.msg=''
            # self.label_2.config(text=self.msg,fg = 'red') 
        self.entry.set('')    
                       



if __name__ == "__main__":
    root = Tk()   
    obj = ChatBot(root)
    root.mainloop()     

