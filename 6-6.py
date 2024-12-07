# The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:

# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
# Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.

parking_time = int(input("Enter the parking time (in hours): "))

if parking_time > 6:
    print("The fee is 20pln")
elif parking_time >= 3:
    print("The fee is 15pln")
elif parking_time >=1:
    print("The fee is 5pln")