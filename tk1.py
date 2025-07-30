import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn= mysql.connector.connect(
		host="localhost",
		user="root",
		password="Root@123",
		database="assignment"
	)

cursor = conn.cursor()

def insert_data():
	fname = entry_name.get()
	email = entry_email.get()
	gender = gender_var.get()
	age = entry_age.get() 

	if fname == "" or email == "" or gender == "" or age == "":
		messagebox.showwarning("All Fields are required")
		return

	try:
		cursor.execute("INSERT INTO emp (fname, email, gender, age) VALUES (%s, %s, %s, %s)",(fname, email, gender, int(age)))
		conn.commit()
		messagebox.showinfo("Success! Data entered SuccessFully")
		entry_name.delete(0,tk.END)
		entry_email.delete(0,tk.END)
		gender_var.delete(0,tk.END)
		entry_age.delete(0,tk.END)
		display_data()
	except Exception as e:
		messagebox.showwarning("Error! Data not entered")


root = tk.Tk()
root.title("Registration Form")

tk.Label(root,text="Full Name").grid(row=0,column=0,padx=10,pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0,column=1,padx=10,pady=5)

tk.Label(root,text="Email").grid(row=1,column=0,padx=10,pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1,column=1,padx=10,pady=5)

tk.Label(root,text="Gender").grid(row=2,column=0,padx=10,pady=5)
gender_var=tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, sticky="e")

tk.Label(root,text="Age").grid(row=3,column=0,padx=10,pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=3,column=1)

tk.Button(root, text="Submit").grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()