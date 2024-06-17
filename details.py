"""
Get user name input
save it in a variable name
Get user age input
Save it to a variable age
type cast age to int
Get user house number
Save user response to a variable house_num
type cast house_num to int
Get user street number
save it to a variable street_name
"""

name = input('Enter your name: ')
age = int(input('How old are you? \n'))
house_num = int(input('What is your house number? \n'))
street_name = input('What is your street name? \n')

print(f"Hello {name}. You're {age} years old, and living in house {house_num} at {street_name}")
