import random

def start_game():
    wager_amount = int(input("Enter wager amount above R10 please!"))

    while wager_amount != 0:
        user_prediction = int(input("Guess a number between 0,100"))
        comp_guess = random.randint(0,100)
        
        if user_prediction == comp_guess:
            print("Congrats!")
            break
        else:
            wager_amount -= 10
            print("Oops you just lost R10, The number was: ",comp_guess,"Try again!")
            print("You have: R",wager_amount,"left")
        exit = input("continue Y/n?")
        if exit == "Y" or "yes":
            continue
        else:
            break

            
    print('You lost all your money,Sorry!')
