# EAN-13 (European Article Number) is a barcode for marking goods. The first 3 digits (590) usually indicate goods manufactured in Poland.
# Write a program that checks whether the EAN-13 number entered from the keyboard consists of exactly 13 characters (digits).
# Print a message if the number is correct.
# Additionally, only when the article number is correct, print a message when the product was manufactured in Poland.
# Sample result:

# Enter EAN-13 article number: 5901230094938
# Article number is correct
# Article manufactured in Poland

ean13 = input("Enter the EAN-13 article number: ")
if len(ean13) == 13:
    print("The article number is correct")
    if "590" in ean13[0:3]:
        print("Article manufactured in Poland")
else:
    print("The article number is incorrect")