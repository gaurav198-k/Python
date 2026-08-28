# Break statement immediately stops the loop and exits it, even if the condition is still True or there are items left in the sequence.

i = 1
while i <= 10:
    print(i, end=" ")
    if i == 5:
        break
    i += 1

print("\n")

for i in range(1, 11):
    if i == 6:
        break
    print(i)
print("\n")    

# Continue statement skips the current iteration and jumps straight to the next one.

i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ") 
print("\n")

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\n")

"""
Take numbers as input from the user one by one. Skip negative numbers and keep adding the positive ones. Stop when the user enters 0 and print the total. (uses both continue and break)
"""

total = 0
while True:
    num = int(input("Enter a number = "))
    if num == 0:
        break        
    if num<=0:
        continue
    total += num
print(total)