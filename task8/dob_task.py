# Read text file
with open('./DOB.txt', 'r') as file:
    content: list[str] = file.readlines()

# Lists to collect separate components of the lines
names: list[list[str]] = []
date_of_births: list[list[str]] =[]

# A loop to split each lines into different components of name and DOB
for item in content:
    splitted = item.split(' ')
    names.append(splitted[:2])
    date_of_births.append(splitted[2:])


# A function that handle printing in human readable format.
def print_readable(lists_to_print: list[list[str]]) -> None:
    for l in lists_to_print:
        print(' '.join(l).strip())
print("Names")
print_readable(names)


print("\n\n\n") #Three newlines for readability


print("Birthdate")
print_readable(date_of_births)
