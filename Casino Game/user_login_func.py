import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, VARCHAR

  
engine = create_engine("postgresql://postgres:postgres@localhost:5430/mafia_casino_db")

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

details = Table(
    'details',meta , 
    Column('user_id', Integer, primary_key=True),
    Column('phone', VARCHAR),
    Column('email', VARCHAR),
    Column('address', VARCHAR),
    extend_existing=True
)

casino_acc = Table(
    'casino_account',meta , 
    Column('user_id', Integer, primary_key=True),
    Column('balance', Integer),
    Column('account_number', Integer),
    extend_existing=True
)

def user_login():

    name = input("Enter Username Please: ")

    user_login_df = pd.DataFrame(engine.execute("SELECT * FROM user_login").fetchall())

    for users in user_login_df[1].to_list():
        if name == users:
            print("Hi",name)
            psswrd = input("Enter your password: ")
            for passw in user_login_df[2].to_list():
                if passw == psswrd:
                    print("Login Successful!")
                    break
            break
        else:
            new_name = input("Enter New Username: ")
            new_psswrd = input("Enter New Password: ")
            statement1 = user.insert().values(username=new_name,password=new_psswrd)
            engine.execute(statement1)
            email_addr = input("Enter New Email: ")
            phone_num = input("Enter Phone Number: ")
            home_address = input("Enter New Address: ")
            statement2 = details.insert().values(phone=phone_num,email=email_addr,address=home_address)
            engine.execute(statement2)
            statement3 = casino_acc.insert().values(balance=0)
            engine.execute(statement3)
            break

