# Let x and y denote the coordinates of a point on the plane.
# Write a program that determines in which quadrant of the coordinate system the point P(x, y)
# is located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system.

# Sample result:
# x = 5
# y = 2
# Point P(5,2) is in the first quadrant of the coordinate system

x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

if x == 0 and y == 0:
    location = "Point P(0,0) is at the origin of the coordinate system."
elif x == 0:
    location = f"Point P({x},{y}) is on the y-axis."
elif y == 0:
    location = f"Point P({x},{y}) is on the x-axis."
elif x > 0 and y > 0:
    location = f"Point P({x},{y}) is in the first quadrant of the coordinate system."
elif x < 0 and y > 0:
    location = f"Point P({x},{y}) is in the second quadrant of the coordinate system."
elif x < 0 and y < 0:
    location = f"Point P({x},{y}) is in the third quadrant of the coordinate system."
else:
    location = f"Point P({x},{y}) is in the fourth quadrant of the coordinate system."

print(location)
