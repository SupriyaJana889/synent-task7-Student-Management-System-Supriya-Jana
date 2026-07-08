import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Database Connection
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT,
    department TEXT,
    semester TEXT,
    email TEXT,
    phone TEXT
)
""")

conn.commit()
# Main Window
root = tk.Tk()
root.title("Student Record Management System")
root.geometry("1000x650")
root.resizable(False, False)
root.configure(bg="#EAF4FC")


title = tk.Label(
    root,
    text="STUDENT RECORD MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#0F4C81",
    fg="white",
    pady=10
)
title.pack(fill="x")
# Student Information Frame
form_frame = tk.LabelFrame(
    root,
    text="Student Information",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=15,
    bg="white"
)
form_frame.place(x=20, y=70, width=960, height=250)
# Labels
tk.Label(form_frame, text="Student ID", bg="white", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Label(form_frame, text="Name", bg="white", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Label(form_frame, text="Age", bg="white", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
tk.Label(form_frame, text="Gender", bg="white", font=("Arial", 11)).grid(row=0, column=2, padx=10, pady=10, sticky="w")
tk.Label(form_frame, text="Department", bg="white", font=("Arial", 11)).grid(row=1, column=2, padx=10, pady=10, sticky="w")
tk.Label(form_frame, text="Semester", bg="white", font=("Arial", 11)).grid(row=2, column=2, padx=10, pady=10, sticky="w")
tk.Label(form_frame, text="Email", bg="white", font=("Arial", 11)).grid(row=0, column=4, padx=10, pady=10, sticky="w")
tk.Label(form_frame, text="Phone", bg="white", font=("Arial", 11)).grid(row=1, column=4, padx=10, pady=10, sticky="w")

student_id_entry = tk.Entry(form_frame, width=20, font=("Arial", 11))
student_id_entry.grid(row=0, column=1, padx=10)

name_entry = tk.Entry(form_frame, width=20, font=("Arial", 11))
name_entry.grid(row=1, column=1, padx=10)

age_entry = tk.Entry(form_frame, width=20, font=("Arial", 11))
age_entry.grid(row=2, column=1, padx=10)

gender_entry = tk.Entry(form_frame, width=20, font=("Arial", 11))
gender_entry.grid(row=0, column=3, padx=10)

department_entry = tk.Entry(form_frame, width=20, font=("Arial", 11))
department_entry.grid(row=1, column=3, padx=10)

semester_entry = tk.Entry(form_frame, width=20, font=("Arial", 11))
semester_entry.grid(row=2, column=3, padx=10)

email_entry = tk.Entry(form_frame, width=20, font=("Arial", 11))
email_entry.grid(row=0, column=5, padx=10)

phone_entry = tk.Entry(form_frame, width=20, font=("Arial", 11))
phone_entry.grid(row=1, column=5, padx=10)
button_frame = tk.Frame(root, bg="#EAF4FC")
button_frame.place(x=20, y=340, width=960, height=70)


def add_student():

    student_id = student_id_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    department = department_entry.get()
    semester = semester_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    
    if (student_id == "" or name == "" or age == "" or
        gender == "" or department == "" or
        semester == "" or email == "" or phone == ""):

        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        cursor.execute("""
            INSERT INTO students
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            student_id,
            name,
            age,
            gender,
            department,
            semester,
            email,
            phone
        ))

        conn.commit()

        messagebox.showinfo(
            "Success",
            "Student added successfully!"
        )

        show_students()
        clear_fields()

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Error",
            "Student ID already exists!"
        )

def update_student():
    pass

def delete_student():
    pass

def search_student():

    student_id = student_id_entry.get()

    if student_id == "":
        messagebox.showerror("Error", "Please enter Student ID")
        return

    cursor.execute(
        "SELECT * FROM students WHERE student_id=?",
        (student_id,)
    )

    row = cursor.fetchone()

    if row:

        clear_fields()

        student_id_entry.insert(0, row[0])
        name_entry.insert(0, row[1])
        age_entry.insert(0, row[2])
        gender_entry.insert(0, row[3])
        department_entry.insert(0, row[4])
        semester_entry.insert(0, row[5])
        email_entry.insert(0, row[6])
        phone_entry.insert(0, row[7])

    else:
        messagebox.showerror("Not Found", "Student not found!")

def clear_fields():

    student_id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def show_students():
    student_table.delete(*student_table.get_children())
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        student_table.insert("", tk.END, values=row)
btn_width = 12
btn_font = ("Arial", 11, "bold")

add_btn = tk.Button(
    button_frame,
    text="Add",
    width=btn_width,
    font=btn_font,
    bg="#4CAF50",
    fg="white",
    command=add_student
)
add_btn.grid(row=0, column=0, padx=10)

update_btn = tk.Button(
    button_frame,
    text="Update",
    width=btn_width,
    font=btn_font,
    bg="#2196F3",
    fg="white",
    command=update_student
)
update_btn.grid(row=0, column=1, padx=10)

delete_btn = tk.Button(
    button_frame,
    text="Delete",
    width=btn_width,
    font=btn_font,
    bg="#F44336",
    fg="white",
    command=delete_student
)
delete_btn.grid(row=0, column=2, padx=10)

search_btn = tk.Button(
    button_frame,
    text="Search",
    width=btn_width,
    font=btn_font,
    bg="#FF9800",
    fg="white",
    command=search_student
)
search_btn.grid(row=0, column=3, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="Clear",
    width=btn_width,
    font=btn_font,
    bg="#9E9E9E",
    fg="white",
    command=clear_fields
)
clear_btn.grid(row=0, column=4, padx=10)

show_btn = tk.Button(
    button_frame,
    text="Show All",
    width=btn_width,
    font=btn_font,
    bg="#673AB7",
    fg="white",
    command=show_students
)
show_btn.grid(row=0, column=5, padx=10)
table_frame = tk.Frame(root, bg="white")
table_frame.place(x=20, y=430, width=960, height=200)
scroll_x = tk.Scrollbar(table_frame, orient="horizontal")
scroll_y = tk.Scrollbar(table_frame, orient="vertical")
student_table = ttk.Treeview(
    table_frame,
    columns=(
        "ID",
        "Name",
        "Age",
        "Gender",
        "Department",
        "Semester",
        "Email",
        "Phone"
    ),
    xscrollcommand=scroll_x.set,
    yscrollcommand=scroll_y.set
)

scroll_x.pack(side="bottom", fill="x")
scroll_y.pack(side="right", fill="y")

scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

student_table.pack(fill="both", expand=True)
student_table.heading("ID", text="Student ID")
student_table.heading("Name", text="Name")
student_table.heading("Age", text="Age")
student_table.heading("Gender", text="Gender")
student_table.heading("Department", text="Department")
student_table.heading("Semester", text="Semester")
student_table.heading("Email", text="Email")
student_table.heading("Phone", text="Phone")


student_table["show"] = "headings"
# Column Widths
student_table.column("ID", width=80, anchor="center")
student_table.column("Name", width=150, anchor="center")
student_table.column("Age", width=60, anchor="center")
student_table.column("Gender", width=80, anchor="center")
student_table.column("Department", width=120, anchor="center")
student_table.column("Semester", width=90, anchor="center")
student_table.column("Email", width=180, anchor="center")
student_table.column("Phone", width=120, anchor="center")

show_students()
root.mainloop()


