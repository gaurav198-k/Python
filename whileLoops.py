#  A loop lets you run the same block of code multiple times without writing it again and again.
# While loop keeps running repeatedly until the condition is false.\

# Print Hello 10 times
i = 1
while i <= 5:
    print("Hello")
    print("Done")
    i += 1
print("\n")

# Print 1 to 10
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print("\n")

# print 1 to n and n is the number input by user
n = int(input("Enter a number: "))
i = 1
while i <= n :
    print(i, end=" ")
    i += 1
print("\n")

# Start and end by user
# Start to end print using while loop

start = int(input("Enter start number: ")) # 5
end = int(input("Enter end number: ")) # 11
i = start
while i <= end:
    print(i, end=" ")
    i += 1
print(f"Ater while loop, start value is {start}")
print("\n")

# start to end print even numbers
start = int(input("Enter start number: "))
end = int(input("Enter end number: ")) 

i = start
while i <= end:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print("\n")

# print start to end, numbers which are divisible by 3 and 4
start = int(input("Enter start number: "))
end = int(input("Enter end number: ")) 

i = start
while i <= end:
    if i % 3 == 0 and i % 4 == 0:
        print(i, end=" ")
    i += 1
print("\n")

#  print 10 to 1
start = int(input("Enter start number: "))
end = int(input("Enter end number: ")) 

if start >= end:
    i = start
    while i >= end:
        print(i, end=" ")
        i -= 1
else:
    i = end
    while i >= start:
        print(i, end=" ")
        i -= 1