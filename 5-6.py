###
# Calculates the sum of even numbers from 1 to a given number N
# The following program calculates the sum of even numbers from 1 to a given number N using a for loop.
# Modify the program. Replace the 'for' statement with a 'while' statement.

N = int(input("Enter the N number: "))
sum_even = 0
even_numbers = 0
i = 1

while i <= N:
    print(i)
    if i % 2 == 0:
        sum_even += i  
        even_numbers += 1
    i += 1


arithmetic_mean = sum_even/even_numbers

print(f"The sum of even numbers from 1 to {N} is: {sum_even}. The arithmetic mean of the numbers is {arithmetic_mean}")