# student.py
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class StudentClass:
    def __init__(self, home):
        self.home = home
        self.home.title("Student Result Management System")
        self.home.geometry("1200x500+80+170")
        self.home.config(bg="white")
        self.home.focus_force()

        title = Label(
            self.home,
            text="Manage Student Details",
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=40)

      
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_adm_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_search = StringVar()

        
        Label(self.home, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        Label(self.home, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        Label(self.home, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        Label(self.home, text="Gender", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=180)

        Label(self.home, text="State", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=220)
        self.state1 = Entry(self.home, textvariable=self.var_state,
                            font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.state1.place(x=150, y=220, width=150)

        Label(self.home, text="City", font=("goudy old style", 15, "bold"), bg="white").place(x=330, y=220)
        self.city1 = Entry(self.home, textvariable=self.var_city,
                           font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.city1.place(x=380, y=220, width=110)

        Label(self.home, text="Pin", font=("goudy old style", 15, "bold"), bg="white").place(x=510, y=220)
        self.pin1 = Entry(self.home, textvariable=self.var_pin,
                          font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.pin1.place(x=560, y=220, width=120)

        Label(self.home, text="Address", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=260)

       
        self.rollno1 = Entry(self.home, textvariable=self.var_roll,
                             font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.rollno1.place(x=150, y=60, width=200)

        Entry(self.home, textvariable=self.var_name,
              font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=100, width=200)
        Entry(self.home, textvariable=self.var_email,
              font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=140, width=200)

        self.gender1 = ttk.Combobox(
            self.home,
            textvariable=self.var_gender,
            values=("Select", "Male", "Female", "Other"),
            font=("goudy old style", 15, "bold"),
            state="readonly",
            justify=CENTER
        )
        self.gender1.place(x=150, y=180, width=200)
        self.gender1.current(0)

        self.address = Text(self.home, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.address.place(x=150, y=260, width=540, height=100)

        
        Label(self.home, text="D.O.B", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=60)
        Label(self.home, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=100)
        Label(self.home, text="Admission", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=140)
        Label(self.home, text="Course", font=("goudy old style", 15, "bold"), bg="white").place(x=360, y=180)

       
        self.course_list = []
        self.fetch_course()

        self.dob1 = Entry(self.home, textvariable=self.var_dob,
                          font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.dob1.place(x=480, y=60, width=200)

        Entry(self.home, textvariable=self.var_contact,
              font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=100, width=200)
        Entry(self.home, textvariable=self.var_adm_date,
              font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=140, width=200)

        self.course1 = ttk.Combobox(
            self.home,
            textvariable=self.var_course,
            values=self.course_list,
            font=("goudy old style", 15, "bold"),
            state="readonly",
            justify=CENTER
        )
        self.course1.place(x=480, y=180, width=200)
        self.course1.set("Select")

       
        self.add_btn = Button(self.home, text="Save",
                              font=("goudy old style", 15, "bold"),
                              bg="#2196f3", fg="white",
                              cursor="hand2", command=self.add)
        self.add_btn.place(x=150, y=400, width=120, height=40)

        self.update_btn = Button(self.home, text="Update",
                                 font=("goudy old style", 15, "bold"),
                                 bg="#4caf50", fg="white",
                                 cursor="hand2", command=self.update)
        self.update_btn.place(x=290, y=400, width=120, height=40)

        self.delete_btn = Button(self.home, text="Delete",
                                 font=("goudy old style", 15, "bold"),
                                 bg="#f44336", fg="white",
                                 cursor="hand2", command=self.delete)
        self.delete_btn.place(x=430, y=400, width=120, height=40)

        self.clear_btn = Button(self.home, text="Clear",
                                font=("goudy old style", 15, "bold"),
                                bg="#607d8b", fg="white",
                                cursor="hand2", command=self.clear)
        self.clear_btn.place(x=570, y=400, width=120, height=40)

        
        Label(self.home, text="Search By Roll No.",
              font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        Entry(self.home, textvariable=self.var_search,
              font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=900, y=60, width=150, height=30)
        Button(self.home, text="Search",
               font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white",
               cursor="hand2", command=self.search).place(x=1060, y=60, width=100, height=30)

        
        self.C_Frame = Frame(self.home, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=360)

        scroly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrolx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(
            self.C_Frame,
            columns=("roll", "name", "email", "gender", "dob", "contact",
                     "admission", "course", "state", "city", "pin", "address"),
            xscrollcommand=scrolx.set,
            yscrollcommand=scroly.set
        )
        scrolx.pack(side=BOTTOM, fill=X)
        scroly.pack(side=RIGHT, fill=Y)
        scrolx.config(command=self.CourseTable.xview)
        scroly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("roll", text="Roll No")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("email", text="Email")
        self.CourseTable.heading("gender", text="Gender")
        self.CourseTable.heading("dob", text="D.O.B")
        self.CourseTable.heading("contact", text="Contact")
        self.CourseTable.heading("admission", text="Admission")
        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("state", text="State")
        self.CourseTable.heading("city", text="City")
        self.CourseTable.heading("pin", text="PIN")
        self.CourseTable.heading("address", text="Address")

        self.CourseTable["show"] = "headings"

        for col in ("roll", "name", "email", "gender", "dob", "contact",
                    "admission", "course", "state", "city", "pin", "address"):
            self.CourseTable.column(col, width=100)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    
    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_adm_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.address.delete("1.0", END)
        self.rollno1.config(state=NORMAL)
        self.var_search.set("")
        self.show()

    def delete(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No should be required", parent=self.home)
            else:
                cur.execute("Select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select the student from the list first", parent=self.home)
                else:
                    p = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.home)
                    if p:
                        cur.execute("Delete from student where roll=?", (self.var_roll.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete", "Student deleted Successfully", parent=self.home)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.home)
        finally:
            conn.close()

    def get_data(self, event):
        self.rollno1.config(state="readonly")
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        if not row:
            return
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_adm_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10])
        self.address.delete("1.0", END)
        self.address.insert(END, row[11])

    def add(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if (self.var_roll.get() == "" or
                    self.var_name.get() == "" or
                    self.var_email.get() == "" or
                    self.var_course.get() == "Select"):
                messagebox.showerror(
                    "Error",
                    "Roll No., Student name, Email and Course are required",
                    parent=self.home
                )
            else:
                cur.execute("Select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Roll No. is already present", parent=self.home)
                else:
                    cur.execute(
                        "Insert into student "
                        "(roll,name,email,gender,dob,contact,admission,course,"
                        "state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_contact.get(),
                            self.var_adm_date.get(),
                            self.var_course.get(),
                            self.var_state.get(),
                            self.var_city.get(),
                            self.var_pin.get(),
                            self.address.get("1.0", END)
                        )
                    )
                    conn.commit()
                    messagebox.showinfo("Great", "Student Added Successfully", parent=self.home)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.home)
        finally:
            conn.close()

    def update(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No should be required", parent=self.home)
            else:
                cur.execute("Select * from student where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select Student From List", parent=self.home)
                else:
                    cur.execute(
                        "Update student set name=?,email=?,gender=?,dob=?,"
                        "contact=?,admission=?,course=?,state=?,city=?,pin=?,"
                        "address=? where roll=?",
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_contact.get(),
                            self.var_adm_date.get(),
                            self.var_course.get(),
                            self.var_state.get(),
                            self.var_city.get(),
                            self.var_pin.get(),
                            self.address.get("1.0", END),
                            self.var_roll.get()
                        )
                    )
                    conn.commit()
                    messagebox.showinfo("Great", "Student Updated Successfully", parent=self.home)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.home)
        finally:
            conn.close()

    def show(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            cur.execute("Select * from student")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.home)
        finally:
            conn.close()

    def fetch_course(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            cur.execute("Select name from course")
            rows = cur.fetchall()
            self.course_list.clear()
            for row in rows:
                self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.home)
        finally:
            conn.close()

    def search(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            cur.execute("Select * from student where roll=?", (self.var_search.get(),))
            row = cur.fetchone()
            if row is not None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert("", END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.home)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.home)
        finally:
            conn.close()
if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()