# The electronic thermometer prints the temperature in degrees Celsius and verbal information according to the following criteria:

# It is extremely hot, for a temperature above 35 degrees,
# It is hot, for a temperature above 30 degrees,
# It is warm, for a temperature of at least 15 degrees,
# It is cold, for a temperature of at least 0 degrees,
# Warning, frost, for a temperature below 0 degrees.
# Write a program that simulates the operation of an electronic thermometer.

# Then check the correctness of the program for the following temperatures in degrees Celsius: 33, 30, 8, 0, -2

###
# Program that simulates the operation of an electronic thermometer.
#
temperature = -2
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
elif temperature >= 0:
    print("It is cold.")
elif temperature < 0: 
    print("Warning, frost")