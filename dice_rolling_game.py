import random


def dice_rolling_game():


    choice = input("Do you want to roll both dice? (y/n): ")

    if choice.upper() == "Y":

        print("Rolling dice 1 and dice 2..: ")
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        print("Dice 1: ", dice_one, " and Dice 2: ", dice_two)
        exit()


    elif choice.upper() == "N":

        print("Thanks for playing game!")
        exit()

    else: 
        print("Invalid input. Please enter 'y' or 'n'.")
        exit()


print(dice_rolling_game())