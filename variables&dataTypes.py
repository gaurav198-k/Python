# A variable is a name that stores a value in the memory
name = "Rahul"
age = 21
gpa = 8.5
is_student = True
print(name)                                                                                                                                                      
print(age)        

# Data Types in Python
# int , float, bool , string
# Int stores whole numbers. Float stores decimal numbers. strig stores Text and the boolean stores True/False values

# Print()
# sep: Changes the seperator between values
print("2026", "08", "17", sep="-")
print("a", "b", "c", sep=" | ")
# end: changes what is printed at the very end
print("Loading", end="...")
print("Done")

# An f-string lets you embed variable values directly inside a string
name = "Karan"
age = 22
course = "Python"
print(f"Hello, {name}. You are {age} years old.")
print(f"Welcome to {course} course")

price = 499
qty = 3
print(f"Total: {price*qty}")

# Type COnversions
# Implicit: Python does it automatically
x = 5
y = 2.0
z = x+y # Python converts x to float automatically
print(z)
print(type(z))
# Explicit: You do it manually
num_str = "42"
num_int = int(num_str)
print(num_str)
num_flt = float(num_str)
print(num_flt)
back_to_str = str(100)
print(back_to_str)

# Taking user input with input()
name = input("Enter your name: ")
print(f"Hello, {name}!")