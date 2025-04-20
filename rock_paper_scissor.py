import random

choice_from_game = ['r', 'p', 's']


# function to continue the game -------------
def continue_game():
    continue_choice = input("Do you want to play again? (y/n): ").lower()

    if continue_choice == 'y':
        print("Let's play again!")
        return True
    
    elif continue_choice == 'n':
        print("Thanks for playing!")
        return False
    
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return continue_game()
        


# Decide the winner -------------
def winner_is(user, computer):
    if user == computer:
        print("It is a Tie!!!")

    elif (user == 'r' and computer == 's') or \
         (user == 'p' and computer == 'r') or \
         (user == 's' and computer == 'p'):
        print("You win!!!")

    else:
        print("You lose!!!")


# main function check the game ----------------

def rock_paper_scissors():
    while True:

        user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()

        guessed = random.choice(choice_from_game)


        if user_choice in choice_from_game:

            print(f'You chose {user_choice}!!')
            print(f'Computer chose {guessed}!!!')
            winner_is(user_choice, guessed)

            if not continue_game():
            # continue_game()
                break


        else:
            print("Invalid choice.")


rock_paper_scissors()