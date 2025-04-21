
first_input = int(input("Enter the first value!!!!"))
second_input = int(input("Enter thr second value!!!!"))

# print(first_input)
# print(second_input)

user_choice = input("Enter your choice (Add/Sub/Mul/Div): ").lower()
# print(user_choice)


if user_choice == str("Add").lower():
    operation =  first_input + second_input
    print(operation)

elif user_choice == str("Sub").lower():
    operation = first_input - second_input
    print(operation)

elif user_choice == str("Mul").lower():
    operation = first_input * second_input
    print(operation)

elif user_choice == str("Div").lower():

    if second_input != 0:
        operation = first_input // second_input
        print(operation)

    else:
        print("Out of bound!!! ")

else:
    print("Invalid choice!! ")