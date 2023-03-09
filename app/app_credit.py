import numpy as np
import pandas as pd
import joblib
import streamlit as st


model = joblib.load('../Models/model_rf_credit.joblib')

st.title('German Credit APP :moneybag:')

name = st.text_input("What is your Name?") 
age = st.text_input("What is your Age", 18,100) 
sex = st.selectbox("Choose sex: (1) Male, (2) Female", [1,2])
credit_amount = st.text_input("Credit Amount",500,100000) 
duration = st.text_input("In how many month you want to pay?",5,72)
account_balance = st.selectbox("Status of existing checking account: (1): < 0 Eu, (2): 0 <= < 400 Eu, (3):  >= 400 Eu , (4): no checking account", [1,2,3,4])
savings = st.selectbox('Total savings: (1): < 200 Eu, (2) between 200 and 1000 Eu, (3) between 1000 and 2000 Eu, (4) >= 2000 Eu, (5) unknown/ no savings account ',[1,2,3,4,5])
property = st.selectbox('Do you have any property? (1) real state, (2), if not the previous, building society savings agreement/ life insurance, (3) if not the previous, car, (4) no property',[1,2,3,4])
guarantors = st.selectbox('Guarantors: (1): no guarantor, (2):co-applicant, (3):guarantor',[1,2,3])
job = st.selectbox('Job Status: (0):unemployed/ unskilled - non-resident, (1):unskilled - resident, (2)skilled employee / official, (3):management/ self-employed/highly qualified employee/ officer',[1,2,3,4])

length_of_current_employment = 1  # (1): unemployed, (2): < 1 year, (3):1 to 4 years, (4): 4 to 7 years, (5): >= 7 years
credit_history = 1
marital_status = 3
concurrent_credits = 3
no_of_credits_at_this_bank = 1
no_of_dependents = 1
telephone = 1
foreign_worker = 2
purpose_business = 0 
purpose_car = 1
purpose_domestic_appliances = 0
purpose_education = 0
purpose_furniture_equipment = 0
purpose_radio_TV = 0
purpose_repairs = 0
purpose_vacation_others = 0
housing_free = 0
housing_own = 0
housing_rent = 1

df = pd.DataFrame({'age':[age],'sex':[sex],'job':[job], 'credit_amount':[credit_amount], 'duration':[duration], 'account_balance':[account_balance],
       'credit_history':[credit_history], 'savings':[savings], 'length_of_current_employment':[length_of_current_employment],
       'marital_status':[marital_status], 'guarantors':[guarantors], 'property':[property], 'concurrent_credits':[concurrent_credits],
       'no_of_credits_at_this_bank':[no_of_credits_at_this_bank], 'no_of_dependents':[no_of_dependents], 'telephone':[telephone],
       'foreign_worker':[foreign_worker], 'purpose_business':[purpose_business], 'purpose_car':[purpose_car],
       'purpose_domestic_appliances':[purpose_domestic_appliances], 'purpose_education':[purpose_education],
       'purpose_furniture_equipment':[purpose_furniture_equipment], 'purpose_radio_tv':[purpose_radio_TV], 'purpose_repairs':[purpose_repairs],
       'purpose_vacation_others':[purpose_vacation_others], 'housing_free':[housing_free], 'housing_own':[housing_own],
       'housing_rent':[housing_rent]})


def predict():
    prob_of_get_the_credit = model.predict_proba(df)[0][1].round(2)
    if prob_of_get_the_credit > 0.6:
        st.success( '{} You have high chances to get the credit :thumbsup: with a probability of {}'.format(name, prob_of_get_the_credit))
    else:
        st.error('{} Your chances are low, try to change some parameter, like the credit amount for example :thumbsdown: with a probability of {}'.format(name, prob_of_get_the_credit)) 

trigger = st.button('Predict', on_click=predict)

if (trigger):
    predict()

#prob_of_get_the_credit = model.predict_proba(df)[0][1].round(2)
#prob_of_get_the_credit