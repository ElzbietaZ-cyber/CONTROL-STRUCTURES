# Write a program that converts a decimal number into a binary number. To convert a decimal number to binary, follow these steps:

# Read a decimal number from the keyboard.
# Divide the number by 2 and note the remainder.
# Divide the quotient obtained by 2 and note the remainder.
# Repeat the same process till we get 0 as the quotient.
# Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.
# Sample result:

# Enter decimal number: 12
# 12(10) = 1100(2)

decimal = int(input("Enter decimal number: "))
original_decimal = decimal 
remainders = []

while decimal > 0:
    remainder = decimal % 2
    remainders.append(str(remainder))  
    decimal = decimal // 2

binary = ''
for i in range(len(remainders) - 1, -1, -1):
    binary += remainders[i]

print(f"{original_decimal}(10) = {binary}(2)")
