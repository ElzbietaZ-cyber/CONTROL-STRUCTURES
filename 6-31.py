# Write a program that prints 20 integer random numbers in the range of 5 to 10.

import random

for num in range(20):
    print(random.randint(5, 10), end=' ')
