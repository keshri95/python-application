import random

num_guess = random.randint(1, 10)


while True:

    try:
        choice = int(input("Guess the number between 1 and 10: "))

        if choice < 1 or choice > 10:
            print("Out of bounds!!!!! ")


        elif choice < num_guess:
            print("Too low!!!! ")

        elif choice > num_guess:
            print("Too high!!!! ")

        
        else:
            print("You guessed it right!!!! ")
            break


    except ValueError:
            print("You entered the string!! ")
