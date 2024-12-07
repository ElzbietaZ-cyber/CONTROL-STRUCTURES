# Write a program that creates the following pattern. Sample result:

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


for i in range(1, 6):
    print('* ' * i)

for i in range(4, 0, -1):
    print('* ' * i)
