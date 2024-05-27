

# Get number of students.
total = int(input("How many students are you registring?\n"))

# open a document named reg_form.txt with a 
# write  mode and assign it to the variable 'file' using.
with open('reg_form.txt', 'w+') as file:
    for i in range(total):
        entry = input('Enter next student\'s ID:\n')
        # write  the student id on its own line at the end with a serial number of i+1.
        # Convert entry to uppercase to ensure consistency in formatting.
        file.write(f"{i+1}. {entry.upper()}: ____________\n") 
