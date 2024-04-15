

# Get number of students.
total: int = int(input("How many students are you registring?\n"))

with open('reg_form.txt', 'w+') as file:
    for i in range(total):
        entry: str = input('Enter next student\'s ID:\n')
        file.write(f"{i+1}. {entry.upper()}: ____________\n") 
