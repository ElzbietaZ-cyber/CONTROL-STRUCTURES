# A washing machine allows you to wash a jacket, which takes 40 minutes, wash underwear, which takes 70 minutes,
# and wash shoes, which takes 20 minutes. In addition, it is possible to program an additional rinse (15 minutes)
#  and an additional spin (9 minutes). The washing machine settings are saved in variables.
# Write a program that calculates and prints the total washing time.

# Sample result:
# washing_product = "shoes"
# rinse = True
# spin = False
# Total washing time: 35 minutes

washing_time = 0

washing_product = input("Enter the washing product (jacket/underwear/shoes): ")
if washing_product.lower() == "jacket":
    washing_time += 40
elif washing_product.lower() == "underwear":
    washing_time += 70
elif washing_product.lower() == "shoes":
    washing_time += 20

rinse = input("Additional rinse? (yes/no): ")
spin = input("Additional spin? (yes/no): ")

if rinse.lower() == "yes":
    washing_time += 15
if spin.lower() == "yes":
    washing_time += 9

print("Total washing time: ", washing_time)