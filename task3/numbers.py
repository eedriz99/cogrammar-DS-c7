# *** Numbers.py ***
# The program recievs three number inputs from the user.
# The program prints out:
#	The sum of all the numbers.
#	The first number minus the second number.
#	The third number multiplied by the first number.
#	The sum of all three numbers divided by the third number.

# ***Algorithm***
#  Get the first input
#  Get the second input
#  Get the third input
#  Print first + second + third
#  Print first - second
#  Print third * first
#  Print (first + second + third)/third

first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
third = int(input('Enter third number: '))

print( f"{ first+second+third = }" )
print(f"{ first-second = }")
print(f"{ third*first = }")
print(f"{(first+second+third)/third = }")
