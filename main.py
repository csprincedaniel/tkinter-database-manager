from tkinter import *

root = Tk()
root.title("Student Database Management System")

frame = LabelFrame(root, text="Student Data")

frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")


Label(frame, text="Name:").grid(row=0, column=0, sticky="w")
name = Entry(frame)
name.grid(row=0, column=1, pady=2, sticky="ew")

Label(frame, text="Address:").grid(row=1, column=0, sticky="w")
address = Entry(frame)
address.grid(row=1, column=1, pady=2, sticky="ew")

Label(frame, text="Age:").grid(row=2, column=0, sticky="w")
age = Entry(frame)
age.grid(row=2, column=1, pady=2, sticky="ew")

Label(frame, text="Number:").grid(row=3, column=0, sticky="w")
number = Entry(frame)
number.grid(row=3, column=1, pady=2, sticky="ew")

root.mainloop()
