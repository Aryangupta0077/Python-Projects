from PIL import ImageTk
from tkinter import *
import PIL.Image
import mysql.connector as msc
from tkinter import messagebox as msg
import time as t
from plyer import notification
import smtplib
mydb = msc.connect(host='localhost', user='root',password='root', database='user_data')
mycursor = mydb.cursor(buffered=True)


class reminder_screen(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.config(bg="#404040")
        self.title("Desktop Reminder App")
        self.title_ = StringVar()
        self.message_ = StringVar()
        self.hrs = IntVar()
        self.mins = StringVar()
        self.r_button = StringVar()
        Label(self, text="Task Reminder", font="MicrosoftYaheiUiLight 20 bold",
              foreground="white", bg="#404040").place(x=120, y=100)
        Label(self, text="Title:", font="MicrosoftYaheiUiLight 15",
              foreground="white", bg="#404040").place(x=50, y=150)
        Entry(self, font="MicrosoftYaheiUiLight 10",
              textvariable=self.title_).place(x=200, y=155)
        Label(self, text="Message:", font="MicrosoftYaheiUiLight 15",
              foreground="white", bg="#404040").place(x=50, y=220)
        Entry(self, font="MicrosoftYaheiUiLight 10",
              textvariable=self.message_).place(x=200, y=220)
        Label(self, text="Time:", font="MicrosoftYaheiUiLight 15",
              bg="#404040", foreground="white").place(x=50, y=290)
        Entry(self, font="MicrosoftYaheiUiLight 10",
              width=5, textvariable=self.hrs).place(x=200, y=290)
        Label(self, text="hrs", font="MicrosoftYaheiUiLight 10",
              foreground="white", bg="#404040").place(x=235, y=290)
        Entry(self, font="MicrosoftYaheiUiLight 10",
              width=5, textvariable=self.mins).place(x=270, y=290)
        Label(self, text="mins", font="MicrosoftYaheiUiLight 10",
              foreground="white", bg="#404040").place(x=310, y=290)
        Radiobutton(self, text="AM", variable=self.r_button,
                    value='am').place(x=350, y=290)
        Radiobutton(self, text="PM", variable=self.r_button,
                    value='pm').place(x=400, y=290)
        Button(self, text="Set", font="MicrosoftYaheiUiLight 10", foreground="white",
               bg="#404040", command=self.set_, width=10, padx=10, pady=10).place(x=150, y=350)

    def set_(self):
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        msg.showinfo("Alert!", "Reminder Set")
        self.state(newstate="iconic")
        title_ = self.title_.get()
        message_ = self.message_.get()
        hrs = self.hrs.get()
        mins = self.mins.get()
        r_button_val = self.r_button.get()
        if hrs == "" or title_ == "" or message_ == "" or mins == "":
            msg.showerror("ERROR", "All fields are Required")
        else:
            if r_button_val == "pm":
                hrs = hrs+12

            reminder_time = f"{hrs}:{mins}"
            current_time = t.strftime("%H:%M")

            while reminder_time != current_time:
                current_time = t.strftime("%H:%M")
            if reminder_time == current_time:

                  notification.notify(title=title_, message=message_,
                                    timeout=10, app_name="Desktop Reminder", toast=False, app_icon="icon_1.ico")

                  s.login("reminderdesktop@gmail.com","kosakyloilczpgrf")
                  s.sendmail("reminderdesktop@gmail.com",email,message_)
                  s.quit()


class login_screen(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1300x600")
        self.config(bg="#FFFFFF")
        self.title("Reminder Application")
        self.maxsize(1300, 600)

        self.icon = ImageTk.PhotoImage(PIL.Image.open("login.jpg"))
        self.icon_label = Label(image=self.icon, bg="white")
        self.icon_label.place(x=25, y=120)

        self.username_value = StringVar()
        self.password_value = StringVar()
        self.email_value_r = StringVar()
        self.username_value_r = StringVar()
        self.password_value_r = StringVar()

        self.f1 = Frame(self, height=500, width=400).place(x=450, y=40)
        self.f2 = Frame(self, height=500, width=400).place(x=870, y=40)

        Label(self.f1, text="Login", font="MicrosoftYaheiUiLight 45",
              bg="#F3F3F3", fg="#57a1f8").place(x=555, y=70)

        Label(self.f1, text="Username *",
              font="MicrosoftYaheiUiLight 15", bg="#F3F3F3", fg="#57a1f8").place(x=465, y=200)
        Entry(self.f1, textvariable=self.username_value,
              font="MicrosoftYaheiUiLight 15").place(x=600, y=199)

        Label(self.f1, text="Password *",
              font="MicrosoftYaheiUiLight 15", fg="#57a1f8").place(x=465, y=299)
        Entry(self.f1, textvariable=self.password_value,
              show="*", font="MicrosoftYaheiUiLight 15").place(x=600, y=299)
        Button(self.f1, text="Login", font="MicrosoftYaheiUiLight 10 bold", command=self.verify,
               fg="#57a1f8", cursor="hand2").place(x=570, y=360)

        Label(self.f2, text="Sign up", font="MicrosoftYaheiUiLight 45",
              bg="#F3F3F3", fg="#57a1f8").place(x=950, y=70)
        Label(self.f2, text="Email *", font="MicrosoftYaheiUiLight 15",
              bg="#F3F3F3", fg="#57a1f8").place(x=900, y=200)
        Entry(self.f2, textvariable=self.email_value_r,
              font="MicrosoftYaheiUiLight 15").place(x=1020, y=199)
        Label(self.f2, text="Username *",
              font="MicrosoftYaheiUiLight 15", bg="#F3F3F3", fg="#57a1f8").place(x=900, y=275)
        Entry(self.f2, textvariable=self.username_value_r,
              font="MicrosoftYaheiUiLight 15").place(x=1020, y=275)
        Label(self.f2, text="Password *",
              font="MicrosoftYaheiUiLight 15", fg="#57a1f8").place(x=900, y=350)
        Entry(self.f2, textvariable=self.password_value_r,
              show="*", font="MicrosoftYaheiUiLight 15").place(x=1020, y=350)
        Button(self.f2, text="Sign up", font="MicrosoftYaheiUiLight 10 bold", command=self.sign_in_,
               fg="#57a1f8", cursor="hand2").place(x=1000, y=425)

    def verify(self):
        uname = self.username_value.get()
        pword = self.password_value.get()
        s1 = "SELECT username from credentials WHERE username=%s"
        s2 = "SELECT password from credentials WHERE password=%s"
        s3 = "SELECT email from credentials WHERE username=%s"
        
        if uname == "" or pword == "":
            msg.showerror("Error", "All fields Required")
        else:
            global email
            mycursor.execute(s1, (uname,))
            user_check = mycursor.fetchone()
            mycursor.execute(s2, (pword,))
            pass_check = mycursor.fetchone()
            mycursor.execute(s3, (uname,))
            email = mycursor.fetchone()
      

        if user_check is None:
            msg.showerror("Error", "User Not Found!")
        elif pass_check is None:
            msg.showerror("Error", "Password is incorrect!")
        else:
            msg.showinfo("Login Success", "Welcome Back!")
            self.destroy()
            reminder = reminder_screen()
            reminder.mainloop()

    def sign_in_(self):
        email_ = self.email_value_r.get()
        uname = self.username_value_r.get()
        pword = self.password_value_r.get()
        l1 = (email_, uname, pword)
        s1 = "SELECT email from credentials WHERE email=%s"
        s2 = "SELECT username from credentials WHERE username=%s"
        if email_ == "" or uname == "" or pword == "":
            msg.showerror("Error", "All fields Required")
        else:
            mycursor.execute(s1, (email_,))
            mycursor.execute(s2, (uname,))
            email_check = mycursor.fetchone()
            user_check = mycursor.fetchone()
            if email_check is None:
                if user_check is None:
                    s = "INSERT INTO credentials (email,username,password) VALUES(%s,%s,%s)"
                    mycursor.execute(s, l1)
                    mydb.commit()
                    msg.showinfo(
                        "Success", "Registered successfully! Now please login")
            else:
                msg.showerror("ERROR", "User already exist")


main_screen = login_screen()
main_screen.mainloop()
