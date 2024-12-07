# Write a program that allows you to convert time in 24-hour format to 12-hour format. 
# The time in 24-hour format (hh:mm) is read from the keyboard. 
# Sample result:

# Enter time (24-hour format): 16:32
# Time in 12-hour format: 4:32pm


time_24 = input("Enter time (24-hour format, hh:mm): ")

hours, minutes = time_24.split(':')
hours = int(hours)  
minutes = int(minutes)  


if hours < 12:
    period = "am"
else:
    period = "pm"


hours_12 = hours % 12
if hours_12 == 0:  
    hours_12 = 12


time_12 = f"{hours_12}:{minutes:02}{period}"
print(f"Time in 12-hour format: {time_12}")
