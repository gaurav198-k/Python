# EScape sequence is a special character that starts with a /. it lets you put things inside a string that are hard to type directly
print("Hello\nWorld") # \n - New line
print("Hello\tWorld") # \t - Tab Space
print("Hel\\lo Wo\\rld") # \\ - Backslash
print("\"hello\" World") # \"Enter text here\" - Double quote
print("\'hello\' World") # \'Enter text here\' - Single quote

print("\n")

# Arithmetic Operators
a = 20
b = 10
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # Floor div gives answer in an int
print(2**5) # Base = 2 , exp = 5 --> 2x2x2x2x2= 32
print(19 % 5) # Remainder is 4
print("\n")

# Operator precedence
# When multiple operators are in one expression, Python follows a specific order
#  Order (highest to lowest)
# ** ---> Exponentiation
# *,/,//,% ---> Multiplication & Division
# +, -   --->  Addition & Substraction

# Without knowing precedence, this looks confusing
print(2 + 3 * 4) # 14, NOT 20 (multiplication first)
print(10 - 2 ** 3) # 2, NOT 512 (exponent first)
print(10 // 2 + 3) # 8, NOT 1
# Use parantheses to force the order you want
print((2 + 3) * 4) # 20
print((10 - 2) ** 3) # 512
print("\n")

# Comparison Operators return a boolean - True or False
a = 10
b = 5
print(a == b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)
print(a != b)
print("\n")

# Logical Operators combine multiple conditions together (and or not)
chemistry = 45
physics = 31
# Print TRUE if pass in both subjects
print(chemistry > 33 and physics > 33)
# Print True if pass in any subjects
print(chemistry > 33 or physics > 33)
print(not chemistry > 33)
print(not chemistry > 33 and not physics > 33)