
def play_again():
    play_game = str(input("Enter your choice (y/n)").lower())

    if play_game == 'y':

        print("Let's play again! ")
        return True
    
    elif play_game == 'n':

        print("Thanks for playing!! ")
        return False
    

    else:
        print("Invalid input. Please enter 'y' or 'n'.")

        return play_again()


# 
def calculator():

    while True:
        try:
            first_input = int(input("Enter the first value!!!!"))
            second_input = int(input("Enter thr second value!!!!"))
            user_choice = str(input("Enter your choice (Add/Sub/Mul/Div): ")).lower()
        
            if user_choice == str("Add").lower():
                operation =  first_input + second_input
                print(f"You have choose {user_choice}: ", operation)
                play_again()


            elif user_choice == str("Sub").lower():
                operation = first_input - second_input
                print(f"You have choose {user_choice}: ", operation)
                # break
                play_again()


            elif user_choice == str("Mul").lower():
                operation = first_input * second_input
                print(f"You have choose {user_choice}: ", operation)
                # break
                play_again()

            elif user_choice == str("Div").lower():

                if second_input != 0:
                    operation = first_input // second_input
                    print(f"You have choose {user_choice}: ", operation)
                    # break
                    play_again()

                else:
                    print("Out of bound!!! ")
                    # break
                    play_again()


            else:
                print("Invalid choice!! ")
                play_again()

        except ValueError:
                print("Please enter integer value! ")


calculator()


