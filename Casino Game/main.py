from start_game_func import start_game
from user_login_func import user_login
from deposit_func import deposit

user_login()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("Welcome to the Grand Mafia Casino:")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("What would you like to do:")

options = input(
        "1. Play game\n"
        "2. Deposit\n"
        "3. Exit\n"
    )

while options is not False:
    
    if options == '1':
        start_game()
        break
    elif options == '2':
        deposit()
        break
    else:
        print("Invalid Option, Please Try Again")
        break