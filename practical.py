# # Initialize primitive data types with descriptive names 
# product_count = 150                    # Integer for counting items 
# total_price = 599.7                    # Float for monetary calculations 
# data_source = "API"                    # String for text data 
# is_active = True                       # Boolean for status flags 
# print(f'product count:{product_count},{type(product_count)}')
# print(f'total_price:{total_price },{type(total_price )}')
# print(f'data_source :{data_source },{type(data_source )}')
# print(f'product count:{is_active},{type(is_active)}')


# import tkinter as tk
# from tkinter import messagebox

# # create the main window (I call it "root")
# root = tk.Tk()
# root.title("Simple login / registration")
# root.geometry("500x300")          # width x height as a string

# # --- Widgets (labels + entries) ---
# tk.Label(root, text="Email:").place(x=20, y=20)
# email_entry = tk.Entry(root)
# email_entry.place(x=120, y=20, width=300)

# tk.Label(root, text="Password:").place(x=20, y=60)
# pwd_entry = tk.Entry(root, show="*")
# pwd_entry.place(x=120, y=60, width=300)

# tk.Label(root, text="Country:").place(x=20, y=100)
# country_entry = tk.Entry(root)
# country_entry.place(x=120, y=100, width=300)

# # A label to show messages (initially empty)
# output_label = tk.Label(root, text="", fg="blue")
# output_label.place(x=20, y=200)

# # --- Function to run when user clicks Register ---
# def registration():
#     # get() must be called with parentheses
#     email = email_entry.get()
#     password = pwd_entry.get()
#     country = country_entry.get()

#     # basic validation
#     if not email or not password:
#         messagebox.showwarning("Missing data", "Please enter email and password.")
#         return

#     # Example: create a message and show it in the output_label
#     message = f"Email: {email}  Country: {country}"
#     output_label.config(text=message)

#     # (Optional) clear the password field after registration
#     pwd_entry.delete(0, tk.END)

# # Register button
# register_btn = tk.Button(root, text="Register", command=registration)
# register_btn.place(x=200, y=150)

# # start the event loop
# root.mainloop()

# screen_resolution = (1920, 1080) 
# sr = list(screen_resolution)
# x = sr.append(1995)
# screen = tuple(sr)
# print(screen)
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# for i in range(5):
#     print(i)


# age = int(input("Enter age: "))
# status = input("Enter status (active/inactive): ")
# score = int(input("Enter score: "))
# Simple if statement for basic validation
# if age < 0:
#     print("Invalid age: cannot be negative")
# else:
#     print("minor")

# if-else for binary decisions
# if age >= 18:
#       user_type = "Adult"
# else:
#      user_type = "Minor"
    # if-elif-else ladder for multiple conditions
# if score >= 90:
#       grade = "A"
# elif score >= 80:
#       grade = "B"
# elif score >= 70:
#       grade = "C"
# else:
#       grade = "F"

# def shadow(func):
#       print("Is running..."); func()


# @shadow
# def truncate():
#       print("Hello World")


# class Person:
#       def __init__(self, firstname, lastname):
#             self.firstname = firstname
#             self.lastname = lastname
      
#       def printname(self):
#             print(self.firstname, self.lastname)

# ptd = Person("John", "Wick")

# class Student(Person):
#       def __init__(self, name, lastname):
#             super().__init__(firstname, lastname)
#             self.graduation_year = 2025

# std = Student("John", "Wick")

# print(std.firstname)


# class School:
#       def __init__(self, name, Class):
#             self.name = name
#             self._class = Class
            
# class Student():
#       def __init__(self, name, Class ):     
#             super().__init__( name, Class)
#             self.subject = subject

#             # self.name = name
#             # self._class = _class
            
      
#       def introduction(self):
#             print(f"I am {self.name} in class {self.Class} studying {self.subject}")

# Student1 = Student("Glad","B","Data Engineering")
# Student1.introduction()

# import time

# while True:
#     Student_name = input("Enter Full_Name: ")
#     score = float(input("Enter score: "))
#     if score < 0 or score > 101:
#         print("invalid")
#     if score >= 90:  
#         grade = "A"
#         print(grade)
#     elif score >= 80:  
#         grade = "B" 
#         print(grade) 
#     elif score >= 70:  
#         grade = "C" 
#         print(grade) 
#     else:  
#         print("F")
#     time.sleep(1)

# student_records = [ 
# {"name": "Alice", "score": 85, "status": "active"}, 
# {"name": "Bob", "score": 92, "status": "inactive"}, 
# {"name": "Carol", "score": 78, "status": "active"}, 
# {"name": "Dave", "score": 65, "status": "active"}
# ]

# """=== For Loop: Processing Student Record==="""
# for student in student_records:
#     if student["status"] == "active":
#         print(f'processing {student['name']}: score {student['score']}')
    
#     else:
#         print('inactive')

# api_calls = 0 
# max_retries = 3 
# success = False 

# words = ['c', 'wind', 'defence']
# for w in words:
#     print(w, len(w))

# for i in range(5):
#     print(i)

x=list(range (-10, -100,))
print(x)