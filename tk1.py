import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="mysql"
)

cursor = conn.cursor()

def insert_data():
    fname = entry_name.get()
    email = entry_email.get()
    gender = gender_var.get()
    age = entry_age.get()

    if fname == "" or email == "" or gender == "" or age == "":
        messagebox.showwarning("Warning", "All fields are required!")
        return

    try:
        cursor.execute(
            "INSERT INTO emp (fname, email, gender, age) VALUES (%s, %s, %s, %s)",
            (fname, email, gender, int(age))
        )
        conn.commit()
        messagebox.showinfo("Success!", "Data entered successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        gender_var.set(None)
        entry_age.delete(0, tk.END)
        display_data()
    except Exception as e:
        messagebox.showerror("Error!", f"Data not entered. {e}")

def display_data():
    # Clear the Text widget first
    text_display.delete(1.0, tk.END)
    try:
        cursor.execute("SELECT fname, email, gender, age FROM emp")
        rows = cursor.fetchall()
        if rows:
            text_display.insert(tk.END, "Saved Records:\n\n")
            for row in rows:
                text_display.insert(tk.END, f"Name: {row[0]}, Email: {row[1]}, Gender: {row[2]}, Age: {row[3]}\n")
        else:
            text_display.insert(tk.END, "No records found.")
    except Exception as e:
        text_display.insert(tk.END, f"Error fetching data: {e}")

root = tk.Tk()
root.title("Registration Form")

tk.Label(root, text="Full Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Gender").grid(row=2, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, sticky="e")

tk.Label(root, text="Age").grid(row=3, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=3, column=1)

tk.Button(root, text="Submit", command=insert_data).grid(row=4, column=0, columnspan=2, pady=10)

# Text widget to display saved data
text_display = tk.Text(root, width=60, height=10)
text_display.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Show existing records on startup
display_data()

root.mainloop()
