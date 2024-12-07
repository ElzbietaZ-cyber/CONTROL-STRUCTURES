# A lamp in a room has three light bulbs. Switch one lights one bulb, and switch two lights the other two bulbs.
# Write a program that tells you how many bulbs are lit, depending on the state of switch one and switch two.

###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
if light_switch1:
    bulbs_on += 1
if light_switch2:
    bulbs_on += 2
print(f"Bulbs on: {bulbs_on}")