# Take a number as input. Print whether it is +ve , -ve, or zero.
num = int(input('Enter a number: '))
if num>0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Equal to zero")
print("\n")

# Take 2 num as input. Print the greater of the 2. If equal, print Both are equal
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print("both are equal")
print("\n")

# Take a year as input. Check if it is a leap year. A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.
# 200 - not a leap year.    204 - leap      800 - leap year

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")