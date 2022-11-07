import random
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, VARCHAR, update
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://postgres:postgres@localhost:5430/mafia_casino_db")

meta = MetaData(bind=engine)
MetaData.reflect(meta)
casino_acc = Table(
    'casino_account',meta , 
    Column('user_id', Integer, primary_key=True),
    Column('balance', Integer),
    Column('account_number', Integer),
    extend_existing=True
)

def start_game():
    acc_number = int(input("Please Enter Account Number: "))
    wager_amount = int(input("Enter wager amount above R10 please!: "))

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
            new_amount = (update(casino_acc).where(casino_acc.c.account_number == acc_number)).values(balance=casino_acc.c.balance - 10)
            engine.execute(new_amount)
        exit = input("continue Y/n?")
        if exit == "Y":
            continue
        else:
            break

            
    print('Game Over!')
    
