# A Conditional statement lets your program to make decisions and execute diff code based on whether a condition is True or False

# If-Else Statement
age = 16
if age >= 18:
    print("You can vote.")
else:
    print("You are too young to vote.")

# If-Elif-Else Stateament
marks = 82
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")

#  Nested If-Else Statement
age = 22
has_degree = False

if age >= 18:
    print("Age requirement met.")
    if has_degree:
        print("You are eligible for this job")
    else:
        print("You need a degree for this job")
else:
    print("You are too young to apply")

# Shorthand if-else (Ternary Operator)
# Python lets you write a simple if-else in a single line. this is called the ternary operator. It is useful when you want to assign a value based on a condition.

# Normal way
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Shorthand way (same result, one line)
age = int(input("Enter age: "))
status = "Adult" if age >= 18 else "Minor"
print(f"Your status is {status}")