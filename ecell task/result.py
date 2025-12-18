from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class ResultClass:
    def __init__(self, home):
        self.home = home
        self.home.title("Student Result Management System")
        self.home.geometry("1200x500+80+170")
        self.home.config(bg="white")
        self.home.focus_force()

        
        title = Label(
            self.home,
            text="Manage Student Results",
            font=("goudy old style", 20, "bold"),
            bg="#FF9500",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=50)

        
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []

        self.fetch_roll()

        
        Label(self.home, text="Select Student",
              font=("goudy old style", 18, "bold"), bg="white").place(x=50, y=100)
        Label(self.home, text="Name",
              font=("goudy old style", 18, "bold"), bg="white").place(x=50, y=160)
        Label(self.home, text="Course",
              font=("goudy old style", 18, "bold"), bg="white").place(x=50, y=220)
        Label(self.home, text="Marks Obtained",
              font=("goudy old style", 18, "bold"), bg="white").place(x=50, y=280)
        Label(self.home, text="Full Marks",
              font=("goudy old style", 18, "bold"), bg="white").place(x=50, y=340)

       
        self.student1 = ttk.Combobox(
            self.home,
            textvariable=self.var_roll,
            values=self.roll_list,
            font=("goudy old style", 15, "bold"),
            state="readonly",
            justify=CENTER
        )
        self.student1.place(x=280, y=100, width=200)
        self.student1.set("Select")

        Button(
            self.home,
            text="Search",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.search
        ).place(x=500, y=100, width=100, height=30)

        Entry(
            self.home,
            textvariable=self.var_name,
            font=("goudy old style", 18, "bold"),
            bg="lightyellow",
            state="readonly"
        ).place(x=280, y=160, width=320, height=30)

        Entry(
            self.home,
            textvariable=self.var_course,
            font=("goudy old style", 18, "bold"),
            bg="lightyellow",
            state="readonly"
        ).place(x=280, y=220, width=320, height=30)

        Entry(
            self.home,
            textvariable=self.var_marks,
            font=("goudy old style", 18, "bold"),
            bg="lightyellow"
        ).place(x=280, y=280, width=320, height=30)

        Entry(
            self.home,
            textvariable=self.var_full_marks,
            font=("goudy old style", 18, "bold"),
            bg="lightyellow"
        ).place(x=280, y=340, width=320, height=30)

        
        Button(
            self.home,
            text="Submit",
            font=("goudy old style", 15, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.add
        ).place(x=300, y=420, width=120, height=35)

        Button(
            self.home,
            text="Clear",
            font=("goudy old style", 15, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.clear
        ).place(x=440, y=420, width=120, height=35)

        
        
        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((530, 300), Image.LANCZOS)
        self.bgImage = ImageTk.PhotoImage(self.bg_img)

        Label(self.home, image=self.bgImage).place(x=640, y=100)


  
    def fetch_roll(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            cur.execute("Select roll from student")
            rows = cur.fetchall()
            self.roll_list = [row[0] for row in rows]
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.home)
        finally:
            conn.close()

    def search(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            cur.execute("Select name,course from student where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row is not None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "No record found", parent=self.home)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.home)
        finally:
            conn.close()

    def add(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror(
                    "Error",
                    "Please first search student record",
                    parent=self.home
                )
            else:
                cur.execute(
                    "Select * from result where roll=? and course=?",
                    (self.var_roll.get(), self.var_course.get())
                )
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Result already present", parent=self.home)
                else:
                    percentage = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())
                    cur.execute(
                        "Insert into result(roll,name,course,marks_obtain,full_marks,percentage) "
                        "values(?,?,?,?,?,?)",
                        (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_marks.get(),
                            self.var_full_marks.get(),
                            f"{percentage:.2f}"
                        )
                    )
                    conn.commit()
                    messagebox.showinfo("Great", "Result Added Successfully", parent=self.home)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.home)
        finally:
            conn.close()

    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")


if __name__ == "__main__":
    home = Tk()
    obj = ResultClass(home)
    home.mainloop()
