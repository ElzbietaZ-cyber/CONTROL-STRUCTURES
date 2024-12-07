# In one of the online stores, a 25% discount is charged for each product purchased over two. 
# Write a program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard.
# Sample result:

# Number of products purchased: 5
# Product price: 40
# Amount to pay: 170.00

import math

purchased_products = int(input("Enter the number of products purchased: "))
product_price = int(input("Enter the price of the products: "))
amount_to_pay = 0



if purchased_products % 2 == 0:
    discounted_products = purchased_products / 2     
    amount_to_pay = (purchased_products-discounted_products)*product_price + discounted_products * product_price * 0.75
else:
    discounted_products = math. ceil(purchased_products / 2)
    amount_to_pay = (purchased_products - discounted_products) * product_price + discounted_products * product_price * 0.75

print("Number of products purchased: ", purchased_products)
print("Product price: ", product_price)
print("Amount to pay: ", amount_to_pay)