# The atm.py program simulates a simple ATM where the user can deposit, withdraw, or check the balance.
# Analyze the program code and then run the program. Next, add two more functions to the program:

# Check PIN
# Change PIN
# The PIN should consist of exactly 4 digits.
# To check if a string contains only digits, you can use the isdigit() method.
# This method returns True if all characters in the string are digits and False otherwise:
# https://www.geeksforgeeks.org/python-string-isdigit-method/

###
# ATM (cash machine) simulator

balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

entered_pin = input("Enter your pin: ")

is_digit = entered_pin.isdigit()
if is_digit == True and entered_pin == pin:
    while True:
        print()
        print("ATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change your pin")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        print()

        if choice == '1':
            print(f"Your current balance is: €{balance}")
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            balance += amount
            print(f"€{amount} has been deposited. New balance: €{balance}")
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"€{amount} has been withdrawn. New balance: €{balance}")
            else:
                print("Insufficient balance.")
        elif choice == '4':
            entered_pin = input("Enter your old pin: ")
            if entered_pin == pin:
                while True:
                    entered_pin = input("Enter your new pin code (it should consist of 4 digits): ")
                    if entered_pin.isdigit() and len(entered_pin) == 4:
                        pin = entered_pin
                        print(f"Your pin is now: {pin}")
                        break
                    else:
                        print("Incorrect pin.")
            else:
                print("Incorrect pin")
        elif choice == '5':
            print("Exiting... Thank you for using the ATM!")
            break  # Exit the loop
        else:
            print("Invalid option. Please try again.")
else:
    print("Incorrect pin")
    
