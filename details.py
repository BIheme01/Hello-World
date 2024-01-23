'''
Task 2

Start

Use the input function to ask the user for the following details:
Name,
Age,
House number, and
Street name

Print out a single sentence with all the user's details

Stop
'''

user_name = input("What is your name? ")
user_age = int(input("What is your age? "))
user_age_str = str(user_age)
house_number = input("What is your house number? ")
street_name = input("What is the name of your street? ")
print("This is " + user_name + "," + " who is " + user_age_str + " years old.", end=" ")
print(user_name + " lives at " + house_number + " "+ street_name +".")

# You can also use f-string instead of concatenation (see below)
print(f"This is {user_name}, who is {user_age_str}years old. {user_name} lives at {house_number} on {street_name}.")