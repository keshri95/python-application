import random
import string

guessed = random.choice(string.ascii_lowercase)
user_choice = input("Rock, Paper, Scissors? (r/p/s) : ").lower()

lists_are = ['r', 'p', 's']


while True:

    try:
        if user_choice == guessed:
            print("You chose Rock!! ")
            break


        elif user_choice == guessed:
            print("You chose Paper!! ")
            break

        elif user_choice == guessed:
            print("You chose Scissors!! ")
            break

        else: 
            print("Invalid choice.")

    except ValueError:
        print("You entered the wrong choice!!!! ")
        break

