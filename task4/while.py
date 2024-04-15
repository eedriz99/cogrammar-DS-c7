# *** ALgorithm ***
# user_input = user input
# user_input_list = []
# while user_input is not equal -1:
#    append user_input to user_input_list
#    user_input = user input
# total = 0
# for i in user_input_list:
#    total = total + i
# print(total)

user_input: int = int(input("Enter a number: "))
user_input_list: list[int] = []
while user_input != -1:
    user_input_list.append(user_input)
    user_input: int = int(input("Enter another number: "))

total: int = 0
for i in user_input_list:
    total += i
print(f"Average = {total/len(user_input_list)}")
