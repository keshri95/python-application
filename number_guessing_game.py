import random

num = input("Guess the number between 1 and 100: ")

if num.isdigit():
    num = int(num)
    
    if num >= 50 and num <= 100:
        print("Too high!!!! ")

    elif num >= 10 and num <= 49:
        print("Too high!!!!!!! ")


    elif num <= 10 and num >= 1:
        print("Too low!!! ")


    elif num == random.randint(1, 9):
        print("Hurray, You guessed the correct number!", num)
        exit()

    else:
        print("Out of bounds !!!!! ")
        exit()

else:
    print("You entered the string!! ")
    exit()
