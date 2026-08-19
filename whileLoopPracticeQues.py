# Sum of all the numbers from 1 to 100 divisible by 2 and 7
start = int(input("Enter start number: "))
end = int(input("Enter end number: ")) 

i = start
total = 0
while i <= end:
    if i % 2 == 0 and i % 7 == 0:
        print(i, end=" ")
        total = total + i             
    i += 1
print(f"Total = {total}")
print("\n")

# Ask a number from the user, print the multiplication table upto 10
num = int(input("Enter a number: "))
i = 1
while i<=10:
    print(f"{num} x {i} = {num*i}")
    i += 1
print("\n")

# Ask a number from the user and print all the factors.
num = int(input("Enter num = "))
i = 1
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1
print("\n")

# Ask a number from the user and count all the factors.
num = int(input("Enter num = "))
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count = count + 1
    i += 1
print(f"Total factors of {num} are {count}")