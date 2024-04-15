# **Algorithm**

# Get participants total time.
# If 0 is less than or equal to time and time is less than or equal to 100:
#	award a Provincial colours
# else if 101 is less than or equal to time and 105 is greater than or equal to time:
#	award a Provincial half colours
# else if 106 is less than or equal to time and 110 is greater than or equal to time:
#	award a Provincial scroll
# else:
#	award Nothing

# *** Code ***

time = int(input('Enter participanty time: '))

if 0 <= time and time <= 100:
	Print("Provincial colours")
elif 100 < time and 105 >= time:
	print("Provincial half colours")
elif 105 < time and time <= 110:
	print("Provincial scroll")
else:
	print("No award")


## https://www.github.com/edriz99
