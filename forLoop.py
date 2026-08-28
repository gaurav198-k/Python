# For Loop --> For loop is used to iterate over a sequence - a range of numbers, a string , a list and so on. Unlike while loop, you don't manage a counter manually - Python handles it for you.

# Looping over a range of numbers
for i in range(1, 6):
    print(i, end=" ")

print("\n")

# 1 3 5 7 9
for i in range(1, 11, 2):
    print(i, end=" ")
print("\n")

# 10 to 1
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")
for i in range(50, 0, -1):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")
print("\n")

# Dynamic for loop 
start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
for i in range(start, end + 1):
    print(i, end=" ")
print("\n")

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
total = 0
for i in range(start, end + 1):
    total += i  
print(total)
