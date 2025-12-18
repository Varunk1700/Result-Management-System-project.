from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

      
        title = Label(
            self.root,
            text="Manage Course Details",
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        )
        title.place(x=10, y=15, width=1180, height=35)

        
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_search = StringVar()

        lbl_courseName = Label(self.root, text="Course Name",
                               font=("goudy old style", 15, "bold"), bg="white")
        lbl_courseName.place(x=10, y=70)

        lbl_duration = Label(self.root, text="Duration",
                             font=("goudy old style", 15, "bold"), bg="white")
        lbl_duration.place(x=10, y=120)

        lbl_charges = Label(self.root, text="Charges",
                            font=("goudy old style", 15, "bold"), bg="white")
        lbl_charges.place(x=10, y=170)

        lbl_description = Label(self.root, text="Description",
                                font=("goudy old style", 15, "bold"), bg="white")
        lbl_description.place(x=10, y=220)

       
        self.courseName1 = Entry(self.root, textvariable=self.var_course,
                                 font=("goudy old style", 15, "bold"),
                                 bg="lightyellow")
        self.courseName1.place(x=150, y=70, width=300)

        txt_duration = Entry(self.root, textvariable=self.var_duration,
                             font=("goudy old style", 15, "bold"),
                             bg="lightyellow")
        txt_duration.place(x=150, y=120, width=300)

        txt_charges = Entry(self.root, textvariable=self.var_charges,
                            font=("goudy old style", 15, "bold"),
                            bg="lightyellow")
        txt_charges.place(x=150, y=170, width=300)

        self.description1 = Text(self.root,
                                 font=("goudy old style", 15, "bold"),
                                 bg="lightyellow")
        self.description1.place(x=150, y=220, width=500, height=100)

        
        self.btn_add = Button(self.root, text="Save",
                              font=("goudy old style", 15, "bold"),
                              bg="#2196f3", fg="white",
                              cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text="Update",
                                 font=("goudy old style", 15, "bold"),
                                 bg="#4caf50", fg="white",
                                 cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete",
                                 font=("goudy old style", 15, "bold"),
                                 bg="#f44336", fg="white",
                                 cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear",
                                font=("goudy old style", 15, "bold"),
                                bg="#607d8b", fg="white",
                                cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

       
        lbl_search_courseName = Label(self.root, text="Course Name",
                                      font=("goudy old style", 15, "bold"),
                                      bg="white")
        lbl_search_courseName.place(x=700, y=70)

        txt_search_courseName = Entry(self.root, textvariable=self.var_search,
                                      font=("goudy old style", 15, "bold"),
                                      bg="lightyellow")
        txt_search_courseName.place(x=830, y=70, width=200)

        btn_search = Button(self.root, text="Search",
                            font=("goudy old style", 15, "bold"),
                            bg="#03a9f4", fg="white",
                            cursor="hand2", command=self.search)
        btn_search.place(x=1040, y=68, width=110, height=35)

        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        scroly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrolx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(
            self.C_Frame,
            columns=("cid", "name", "duration", "charges", "description"),
            xscrollcommand=scrolx.set,
            yscrollcommand=scroly.set,
            show="headings"
        )

        scrolx.pack(side=BOTTOM, fill=X)
        scroly.pack(side=RIGHT, fill=Y)
        scrolx.config(command=self.CourseTable.xview)
        scroly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("cid", text="CID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("description", text="Description")

        self.CourseTable.column("cid", width=50)
        self.CourseTable.column("name", width=120)
        self.CourseTable.column("duration", width=80)
        self.CourseTable.column("charges", width=80)
        self.CourseTable.column("description", width=140)

        self.CourseTable.pack(fill=BOTH, expand=1)

        self.CourseTable.bind("<<TreeviewSelect>>", self.get_data)

        self.show()

    
    def clear(self):
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.description1.delete("1.0", END)
        self.courseName1.config(state=NORMAL)
        self.show()

    def get_data(self, event):
        self.courseName1.config(state="readonly")
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        if not row:
            return
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.description1.delete("1.0", END)
        self.description1.insert(END, row[4])

    def add(self):
        conn = sqlite3.connect("ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Course name should be required", parent=self.root
                )
            else:
                cur.execute("SELECT * FROM course WHERE name=?",
                            (self.var_course.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror(
                        "Error",
                        "Course name already present",
                        parent=self.root
                    )
                else:
                    cur.execute(
                        "INSERT INTO course (name,duration,charges,description) "
                        "VALUES (?,?,?,?)",
                        (
                            self.var_course.get(),
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.description1.get("1.0", END)
                        )
                    )
                    conn.commit()
                    messagebox.showinfo(
                        "Success",
                        "Course added successfully",
                        parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",
                                 parent=self.root)
        finally:
            conn.close()

    def update(self):
        conn = sqlite3.connect("ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Course name should be required", parent=self.root
                )
            else:
                cur.execute("SELECT * FROM course WHERE name=?",
                            (self.var_course.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error",
                        "Select course from list",
                        parent=self.root
                    )
                else:
                    cur.execute(
                        "UPDATE course SET duration=?, charges=?, description=? "
                        "WHERE name=?",
                        (
                            self.var_duration.get(),
                            self.var_charges.get(),
                            self.description1.get("1.0", END),
                            self.var_course.get()
                        )
                    )
                    conn.commit()
                    messagebox.showinfo(
                        "Success",
                        "Course updated successfully",
                        parent=self.root
                    )
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",
                                 parent=self.root)
        finally:
            conn.close()

    def delete(self):
        conn = sqlite3.connect("ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror(
                    "Error", "Course name should be required", parent=self.root
                )
            else:
                cur.execute("SELECT * FROM course WHERE name=?",
                            (self.var_course.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error",
                        "Select the course from the list first",
                        parent=self.root
                    )
                else:
                    p = messagebox.askyesno(
                        "Confirm", "Do you really want to delete?",
                        parent=self.root
                    )
                    if p:
                        cur.execute("DELETE FROM course WHERE name=?",
                                    (self.var_course.get(),))
                        conn.commit()
                        messagebox.showinfo(
                            "Delete",
                            "Course deleted successfully",
                            parent=self.root
                        )
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",
                                 parent=self.root)
        finally:
            conn.close()

    def show(self):
        conn = sqlite3.connect("ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",
                                 parent=self.root)
        finally:
            conn.close()

    def search(self):
        conn = sqlite3.connect("ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            cur.execute(
                "SELECT * FROM course WHERE name LIKE ?",
                (f"%{self.var_search.get()}%",)
            )
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",
                                 parent=self.root)
        finally:
            conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
