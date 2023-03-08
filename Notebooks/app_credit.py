import numpy as np
import pandas as pd
import joblib
import streamlit as st


model = joblib.load('../Models/model_rf_credit.joblib')

st.title('German Credit APP :moneybag:')

name = st.text_input("What is your Name?") 
age = st.text_input("What is your Age") 
sex = st.selectbox("Choose sex: (1) Male, (2) Female", [1,2])
credit_amount = st.text_input("Credit Amount",0,100000) 
duration = st.text_input("In how many month you want to pay?",5,72)
account_balance = st.selectbox("Status of existing checking account: (1): < 0 Eu, (2): 0 <= < 400 Eu, (3):  >= 400 Eu , (4): no checking account", [1,2,3,4])



savings = 3 #total savings. (1): < 200 Eu, (2) between 200 and 1000 Eu, (3) between 1000 and 2000 Eu, (4) >= 2000 Eu, (5) unknown/ no savings account 
property = 3 #  (1) real state, (2), if not the previous, building society savings agreement/ life insurance, (3) if not the previous, car, (4) no property
guarantors = 0 #(1): no guarantor, (2):co-applicant, (3):guarantor
job = 1 # (0):unemployed/ unskilled - non-resident, (1):unskilled - resident, (2)skilled employee / official, (3):management/ self-employed/highly qualified employee/ officer