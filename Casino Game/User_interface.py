import random
import streamlit as st
import pandas as pd
from sqlalchemy import VARCHAR, Column, Integer, MetaData, Table,create_engine, update, select

st.set_page_config(layout="centered",initial_sidebar_state="collapsed",page_title="Grand Mafia Casino",page_icon="🎲")
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
        wager_amount = st.slider("Enter wager amount between R10 and R1000 please!: ",min_value=10,max_value=1000)

        user_prediction = st.slider("Guess a number between 0,100",min_value=0,max_value=100)
        comp_guess = float(random.randint(0,100))
        submit = st.form_submit_button("Guess")
        if submit:
            if user_prediction == comp_guess:
                st.write("Congrats!")
            else:
                st.write("Oops you just lost R",wager_amount," The number was: ",comp_guess,"Try again!")
                new_amount = (update(casino_acc).where(casino_acc.c.account_number == acc_number)).values(balance=casino_acc.c.balance - wager_amount)
                engine.execute(new_amount)
                acc_df = pd.DataFrame(engine.execute("SELECT * FROM casino_account").fetchall())
                st.write("You Have R",acc_df[1][acc_number],"left in your Casino account")
                
def deposit():
    amount = st.number_input("Enter Amount to deposit in Rands: ")
    acc_number = st.number_input("Enter Account Number: ")
    with st.form('deposit'):
        submit_deposit= st.form_submit_button("Deposit!")
        if submit_deposit:
            new_amount = (update(casino_acc).where(casino_acc.c.account_number == acc_number)).values(balance=casino_acc.c.balance + amount)
            engine.execute(new_amount)
            acc_df = pd.DataFrame(engine.execute("SELECT * FROM casino_account").fetchall())
            st.write("You Have R",acc_df[1][acc_number],"in your Casino account")
            

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
st.markdown("<p style='text-align: center; color: white;'>1. Start game</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>2. Deposit</p>", unsafe_allow_html=True)
st.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



options = st.text_input('Enter option')

if options == '1':
    start_game()

elif options == '2':
    deposit()

                


