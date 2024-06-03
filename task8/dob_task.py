# Read text file
with open('./DOB.txt', 'r') as file:
    content = file.readlines()

# Lists to collect separate components of the lines
names = []
date_of_births =[]

# A loop to split each lines into different components of name and DOB
for item in content:
    splitted = item.split(' ')
    #split every item in the content  by a space, 
    # then add it to its respective list to variables names and  date_of_births
    names.append(splitted[:2])
    date_of_births.append(splitted[2:])


# A function that handle printing in human readable format.
def print_readable(lists_to_print):
    for l in lists_to_print:
        # join every elements with space
        print(' '.join(l).strip())
print("***** Names *****")
print_readable(names)


print("\n\n\n") #Three newlines for readability


print("***** Birthdates *****")
print_readable(date_of_births)
