import random
import streamlit as st
import pandas as pd
from sqlalchemy import VARCHAR, Column, Integer, MetaData, Table,create_engine, update, select

st.set_page_config(layout="centered",initial_sidebar_state="auto")
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

casino_acc = Table(
    'casino_account',meta , 
    Column('user_id', Integer, primary_key=True),
    Column('balance', Integer),
    Column('account_number', Integer),
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


def start_game():
    with st.form("game"):
        acc_number = st.number_input("Please Enter Account Number: ")
        wager_amount = st.number_input("Enter wager amount above R10 please!: ")

        user_prediction = st.number_input("Guess a number between 0,100")
        comp_guess = random.randint(0,100)
        st.form_submit_button("Guess")
    
        if user_prediction == comp_guess:
            st.write("Congrats!")
        else:
            st.write("Oops you just lost ",wager_amount," The number was: ",comp_guess,"Try again!")
            st.write("You have: R",wager_amount,"left")
            new_amount = (update(casino_acc).where(casino_acc.c.account_number == acc_number)).values(balance=casino_acc.c.balance - wager_amount)
            engine.execute(new_amount)
    
       
def deposit():
    amount = st.number_input("Enter Amount to deposit in Rands: ")
    acc_number = st.text_input("Enter Account Number: ")
    with st.form('deposit'):
        submit_deposit= st.form_submit_button("Deposit!")
        if submit_deposit:
            new_amount = (update(casino_acc).where(casino_acc.c.account_number == acc_number)).values(balance=casino_acc.c.balance + amount)
            engine.execute(new_amount)

sb = st.sidebar.success(body='Please Login before you Play game!')
with st.sidebar:
    with st.form(key='user_login'):
        name = st.text_input("Enter Username Please: ")

        user_login_df = pd.DataFrame(engine.execute("SELECT * FROM user_login").fetchall())
        for users in user_login_df[1].to_list():
                if name == users:
                    psswrd = st.text_input("Enter your password: ")
        sumbit_username = st.form_submit_button("Login!")
        if sumbit_username:
            for passw in user_login_df[2].to_list():
                if passw == psswrd:
                    st.write("Login Successful!")
                    st.balloons()
                    break
st.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
st.markdown("<h1 style='text-align: center; color: white;'>Grand Mafia Casino</h1>", unsafe_allow_html=True)
st.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
st.markdown("<h2 style='text-align: center; color: white;'>Welcome!</h2>", unsafe_allow_html=True)
st.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    game = st.button("1. Start Game",)
    depositing = st.button("2. Deposit   ")
    exit = st.button("3. Exit")
st.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
while exit is not True:
    if game:
        start_game()
        break
    if depositing:
        deposit()
        break
                


