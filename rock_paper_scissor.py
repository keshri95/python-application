import random

choice_from_game = ['r', 'p', 's']

user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()

guessed = random.choice(choice_from_game)



def winner_is(user, computer):
    if user == computer:
        print("It is a Tie!!!")

    elif (user == 'r' and computer == 's') or \
         (user == 'p' and computer == 'r') or \
         (user == 's' and computer == 'p'):
        print("You win!!!")

    else:
        print("You lose!!!")



if user_choice in choice_from_game:

    print(f'You chose {user_choice}!!')
    print(f'Computer chose {guessed}!!!')
    winner_is(user_choice, guessed)


else:
    print("Invalid choice.")
