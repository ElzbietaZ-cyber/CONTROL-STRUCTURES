###
# The timer.py program takes a number from the user and counts down to zero.
# Modify the program so that the last five seconds of the counter are printed in words, i.e. five, four, three, two, one.

number = int(input("Enter the number: "))

for i in range(number, 0, -1):
    if i > 5:
        print(i)
    else:
        if i == 5:
            print("five")
        elif i == 4:
            print("four")
        elif i == 3:
            print("three")
        elif i == 2:
            print("two")
        elif i == 1:
            print("one")
