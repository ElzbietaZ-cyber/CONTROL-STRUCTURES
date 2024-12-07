# There are coins of 1, 2 and 5 Polish Zlotys (PLN).
# Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

# Enter the amount in PLN: 18
# The amount of PLN 18 in coins:
# 5 PLN coins: 3
# 2 PLN coins: 1
# 1 PLN coins: 1

amount = int(input("Enter the amount in PLN: "))

five_pln = amount // 5
amount = amount % 5

two_pln = amount // 2
amount = amount % 2

one_pln = amount // 1

print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {five_pln}")
print(f"2 PLN coins: {two_pln}")
print(f"1 PLN coins: {one_pln}")
