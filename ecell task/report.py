from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3


class ViewClass:
    def __init__(self, home):
        self.home = home
        self.home.title("Student Result Management System")
        self.home.geometry("1200x500+80+170")
        self.home.config(bg="white")
        self.home.focus_force()

        
        title = Label(
            self.home,
            text="View Student Results",
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=50)

        
        self.var_search = StringVar()
        self.var_id = ""

        Label(
            self.home,
            text="Select By Roll No.",
            font=("goudy old style", 18, "bold"),
            bg="white"
        ).place(x=260, y=100)

        Entry(
            self.home,
            textvariable=self.var_search,
            font=("goudy old style", 18),
            bg="lightyellow"
        ).place(x=500, y=100, width=150, height=30)

        Button(
            self.home,
            text="Search",
            font=("goudy old style", 15, "bold"),
            bg="#2196f3",
            fg="white",
            cursor="hand2",
            command=self.search
        ).place(x=660, y=100, width=100, height=30)

        Button(
            self.home,
            text="Clear",
            font=("goudy old style", 15, "bold"),
            bg="#4caf50",
            fg="white",
            cursor="hand2",
            command=self.clear
        ).place(x=780, y=100, width=100, height=30)

        
        head_font = ("goudy old style", 15, "bold")

        Label(
            self.home, text="Roll No.", font=head_font,
            bg="white", bd=2, relief=GROOVE
        ).place(x=150, y=230, width=150, height=50)

        Label(
            self.home, text="Name", font=head_font,
            bg="white", bd=2, relief=GROOVE
        ).place(x=300, y=230, width=150, height=50)

        Label(
            self.home, text="Course", font=head_font,
            bg="white", bd=2, relief=GROOVE
        ).place(x=450, y=230, width=150, height=50)

        Label(
            self.home, text="Marks Obtained", font=head_font,
            bg="white", bd=2, relief=GROOVE
        ).place(x=600, y=230, width=150, height=50)

        Label(
            self.home, text="Total Marks", font=head_font,
            bg="white", bd=2, relief=GROOVE
        ).place(x=750, y=230, width=150, height=50)

        Label(
            self.home, text="Percentage", font=head_font,
            bg="white", bd=2, relief=GROOVE
        ).place(x=900, y=230, width=150, height=50)

        self.roll = Label(
            self.home, font=head_font,
            bg="white", bd=2, relief=GROOVE
        )
        self.roll.place(x=150, y=280, width=150, height=50)

        self.name = Label(
            self.home, font=head_font,
            bg="white", bd=2, relief=GROOVE
        )
        self.name.place(x=300, y=280, width=150, height=50)

        self.course = Label(
            self.home, font=head_font,
            bg="white", bd=2, relief=GROOVE
        )
        self.course.place(x=450, y=280, width=150, height=50)

        self.marks = Label(
            self.home, font=head_font,
            bg="white", bd=2, relief=GROOVE
        )
        self.marks.place(x=600, y=280, width=150, height=50)

        self.full = Label(
            self.home, font=head_font,
            bg="white", bd=2, relief=GROOVE
        )
        self.full.place(x=750, y=280, width=150, height=50)

        self.percentage = Label(
            self.home, font=head_font,
            bg="white", bd=2, relief=GROOVE
        )
        self.percentage.place(x=900, y=280, width=150, height=50)

        
        Button(
            self.home,
            text="Delete",
            font=("goudy old style", 15, "bold"),
            bg="#f44336",
            fg="white",
            cursor="hand2",
            command=self.delete
        ).place(x=520, y=360, width=150, height=35)

    def search(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror(
                    "Error", "Roll No. should be required", parent=self.home
                )
            else:
                cur.execute(
                    "SELECT * FROM result WHERE roll=?",
                    (self.var_search.get(),)
                )
                row = cur.fetchone()
                if row is not None:
                 
                    self.var_id = row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.percentage.config(text=row[6])
                else:
                    messagebox.showerror(
                        "Error", "No record found", parent=self.home
                    )
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to {str(ex)}", parent=self.home
            )
        finally:
            conn.close()

    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")

    def delete(self):
        conn = sqlite3.connect(database="ResultManagementSystem.db")
        cur = conn.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror(
                    "Error", "Search student result first", parent=self.home
                )
            else:
                cur.execute("SELECT * FROM result WHERE rid=?", (self.var_id,))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror(
                        "Error", "Invalid student result", parent=self.home
                    )
                else:
                    p = messagebox.askyesno(
                        "Confirm", "Do you really want to delete?", parent=self.home
                    )
                    if p:
                        cur.execute(
                            "DELETE FROM result WHERE rid=?",
                            (self.var_id,)
                        )
                        conn.commit()
                        messagebox.showinfo(
                            "Delete", "Result deleted successfully", parent=self.home
                        )
                        self.clear()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to {str(ex)}", parent=self.home
            )
        finally:
            conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = ViewClass(root)
    root.mainloop()
