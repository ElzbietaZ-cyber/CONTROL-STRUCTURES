# A computer program analyses the price of a product in an online store.
# If the product price decreases by at least 10%, the program prints a purchase recommendation:

# Buy the product!!
# Product price reduced by 17%
# Create such program. The current and previous price of the product are included in variables. Sample result:

# Current product price: 140.00
# Previous product price: 200.00
# Buy the product!!
# Product price reduced by 30%

current_price = float(input("Enter the current price: "))
previous_price = float(input("Enter the previous price: "))
reduction = ((previous_price - current_price)/previous_price)*100
    

print(f"Current product price: {current_price}")
print(f"Previous product price: {previous_price}")

if current_price < previous_price and reduction >= 10:
    print("Buy the product!!")
    print(f"Product reduced by {reduction}%")
else:
    print("Don't buy it.")

