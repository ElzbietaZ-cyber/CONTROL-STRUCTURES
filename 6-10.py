# Write a program that calculates a dog's age in dog's years.
# For the first two years, a dog's life is equal to 10.5 human years.
# After that, each dog year is equal to 4 human years. Sample result:

# Enter the dog's age in human years: 15
# The dog's age in dog's years is 73 years.

age = int(input("Enter the dog's age in human years: "))
age_counter = 1
dog_years = 0.0 

while age_counter <= age:
    if age_counter <= 2 :
        dog_years += 10.5
    if age_counter > 2:
        dog_years += 4
    age_counter += 1

print(f"The dog's age in dog's years is {dog_years}")
