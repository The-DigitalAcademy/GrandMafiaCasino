from sqlalchemy import create_engine, MetaData, Table, Column, Integer, VARCHAR, update
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://postgres:postgres@localhost:5430/mafia_casino_db")

casino_df = pd.read_sql_table("casino_account",con=engine,columns=['user_id','balance'])
  
  
# initialize the Metadata Object
meta = MetaData(bind=engine)
MetaData.reflect(meta)
  
# create a table schema
# create a table schema
user = Table(
    'user_login',meta , 
    Column('user_id', Integer, primary_key=True),
    Column('username', VARCHAR),
    Column('password', VARCHAR),
    extend_existing=True
)

casino_acc = Table(
    'casino_account',meta , 
    Column('user_id', Integer, primary_key=True),
    Column('balance', Integer),
    Column('account_number', Integer),
    extend_existing=True
)


def deposit():
    amount = int(input("Enter Amount to deposit in Rands: "))
    name = input("Please Enter username to Confirm: ")
    acc_number = int(input("Enter Account Number: "))
    user_login_df = pd.DataFrame(engine.execute("SELECT * FROM user_login").fetchall())

    while user_login_df[1].str.contains(name).any():
        new_amount = (update(casino_acc).where(casino_acc.c.account_number == acc_number)).values(balance=casino_acc.c.balance + amount)
        engine.execute(new_amount)
        break
    
    return print("Deposit Done!")