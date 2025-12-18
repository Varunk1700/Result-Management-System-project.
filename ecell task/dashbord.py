from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ViewClass
from create_db import create_db  
import sqlite3

create_db() 

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

     
        title = Label(
            self.root,
            text="Student Result Management System",
            padx=10,
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white",
        )
        title.place(x=0, y=0, relwidth=1, height=50)

        
        M_Frame = LabelFrame(
            self.root,
            text="Menus",
            font=("times new roman", 15),
            bg="white"
        )
        M_Frame.place(x=10, y=70, width=1340, height=80)

        btn_course = Button(
            M_Frame,
            text="Course",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_course
        )
        btn_course.place(x=20, y=5, width=200, height=40)

        btn_student = Button(
            M_Frame,
            text="Student",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_student
        )
        btn_student.place(x=240, y=5, width=200, height=40)

        btn_result = Button(
            M_Frame,
            text="Result",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_result
        )
        btn_result.place(x=460, y=5, width=200, height=40)

        btn_view = Button(
            M_Frame,
            text="View Student Results",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_report
        )
        btn_view.place(x=680, y=5, width=250, height=40)

        btn_logout = Button(
            M_Frame,
            text="Logout",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.logout
        )
        btn_logout.place(x=950, y=5, width=150, height=40)

        btn_exit = Button(
            M_Frame,
            text="Exit",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.exit
        )
        btn_exit.place(x=1120, y=5, width=150, height=40)

        
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=400, y=180, width=920, height=350)

       
        self.lbl_course = Label(
            self.root,
            text="Total Courses\n[ 0 ]",
            font=("goudy old style", 20),
            bg="#e43b06",
            relief=RIDGE,
            bd=10,
            fg="white"
        )
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(
            self.root,
            text="Total Students\n[ 0 ]",
            font=("goudy old style", 20),
            bg="#0676ad",
            relief=RIDGE,
            bd=10,
            fg="white"
        )
        self.lbl_student.place(x=720, y=530, width=300, height=100)

        self.lbl_result = Label(
            self.root,
            text="Total Results\n[ 0 ]",
            font=("goudy old style", 20),
            bg="#038074",
            relief=RIDGE,
            bd=10,
            fg="white"
        )
        self.lbl_result.place(x=1040, y=530, width=300, height=100)
        
        self.footer = Label(
            self.root,
            text="Student Result Management System",
            font=("times new roman", 12, "bold"),
            bg="grey",
            fg="white"
        )
        self.footer.pack(side=BOTTOM, fill=X)

        self.update_details()

    
    def update_details(self):
        conn = sqlite3.connect("ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[ {len(cr)} ]")

            cur.execute("SELECT * FROM student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[ {len(cr)} ]")

            cur.execute("SELECT * FROM result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[ {len(cr)} ]")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            conn.close()

       
        self.root.after(2000, self.update_details)

    
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win2 = Toplevel(self.root)
        self.new_obj2 = StudentClass(self.new_win2)

    def add_result(self):
        self.new_win3 = Toplevel(self.root)
        self.new_obj3 = ResultClass(self.new_win3)

    def add_report(self):
        self.new_win4 = Toplevel(self.root)
        self.new_obj4 = ViewClass(self.new_win4)

   
    def logout(self):
        op = messagebox.askyesno(
            "Confirm Again",
            "Do you really want to Logout?",
            parent=self.root
        )
        if op:
            messagebox.showinfo("Logged Out", "You have been logged out successfully!", parent=self.root)
            self.root.destroy()  

    
    def exit(self):
        op = messagebox.askyesno(
            "Confirm Again",
            "Do you really want to Exit?",
            parent=self.root
        )
        if op:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
