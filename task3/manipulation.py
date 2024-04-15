"""
Get user input and save its value in variable str_manip
Calculate the length of the input
Determine the last character of the user input using the negative index
Replace all occurence of the last character in the input with @ using for loop and condition.
Print the last 3 characters in str_manip backwards using the reverse method of the strigng datatype
Create a 5 letter word using the first 3 characters and the last 3 characters of str_manip utilizing the string slicing with index
"""

str_manip = input('Input a string of your choice: ')
print(len(str_manip))
last_char = str_manip[-1]

temp=''
for char in str_manip:
    if char != last_char:
        temp += char
    else:
        temp += '@'
print(temp)

# or

# str_manip.replace(last_char, '@')

print(str_manip[-1:-3:-1])

print(str_manip[:3] + str_manip[-2:])
