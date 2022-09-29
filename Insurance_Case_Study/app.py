#core packages
from copyreg import pickle
import imp
from msilib import add_data
from msilib.schema import Property
import streamlit as st
import altair as alt
import plotly.express as px

#import EDA pkgs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from datetime import datetime
#utility files
from utils import *
import os 
from manage_db import *
#def load_model(model_file):
import joblib

# track utilities

# feature columns for the predictions
SelectedColumns = ['Foreign_Worker', 'Sex','Status', 'Credit history', 'Saving_acccount_bonds', 'Installment_Rate', 'Debtors_Guarantors', 'Property', 'Other_Installment_Plans',
 'Housing','Duration', 'Age', 'Credit_Amount', 'Installment_Rate/Income']


# dictionaries that we use for the encoding 
# making ML processing easier
gender_dict = {"male":1, "female":0}
worker_dict  = {'Yes':1, 'No':0}
status = {'single':0, 'divorced/separated/married':1, 'divorced/separated':2,'married/widowed':3}
credit_history = {'critical account/ other credits existing (not at this bank)':0,
       'existing credits paid back duly till now':1,
       'delay in paying off in the past':2,
       'no credits taken / all credits paid back duly':3,
       'all credits at this bank paid back duly':4}
savings_account_bond = {'unknown / no savings account':0, 'less than 100':1, '500 to 1000':2,
       'more than 1000':3, '100 to 500':4}
installmentRate = {'more than 7 years':0, '1 to 4 years':1, '4 to 7 years':2, 'Unemployed':3,'less than 1 year':4}
debtorsGuarantors = {'none':0, 'guarantor':1, 'co-Applicant':2}
property_dict = {'real estate':0,'building society savings agreement/ life insurance':1,
       'unknown / no property':2, 'car or other':3}
other_installment_plans = {'none':0, 'bank':1, 'stores':2}
housing = {'own':0, 'for free':1, 'rent':2}


data = pd.read_csv('case_hepster_clean.csv')

def load_model(model_file):
    """ load the ML model"""
    loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_model

def main():
    """ Credit Score prediction"""
    st.title('Credit Score Classifier')
    Menu = ["Home", "Monitor", "About"]
    choice = st.sidebar.selectbox("Menu", Menu)
    page_visit()
    track_review()
    if choice == "Home":
        add_data("Home", datetime.now())
        st.subheader('Customer review')
        with st.form(key = 'customer_form', clear_on_submit= True):
            Foreign_worker = st.radio('Are you a foreign worker?', tuple(worker_dict.keys()))
            Gender = st.radio('What is your Gender ?', tuple(gender_dict.keys()))
            Status = st.selectbox('What is the status of your checking account?', tuple(status.keys()))
            Credit_Hist = st.selectbox('Which text best describes your credit history', tuple(credit_history.keys()))
            SvgBond = st.selectbox('Do you have a savings account or a Bond?', tuple(savings_account_bond.keys()))
            InstallmentRate = st.selectbox('What is your current installment rate ?', tuple(installmentRate.keys()))
            DebtGuarantors = st.selectbox('Indicate if you have a guarantor Status', tuple(debtorsGuarantors.keys()))
            PropertyValue = st.selectbox('Indicate your current property', tuple(property_dict.keys()))
            otherInstallmentPlans = st.selectbox('Do you have other installment plans', tuple(other_installment_plans.keys()))
            Housing = st.selectbox('What is your housing status', tuple(housing.keys()))
            Duration = st.number_input('How long have you been a customer', 0, 72)
            Age = st.number_input('Indicate your age', 18 , 90)
            CreditAmount = st.number_input('Indicate your Credit Amount', 0, 100000)
            installmentRateIncome = data['Installment_Rate/Income'].sort_values().unique()
            InstallmentRateIncome = st.number_input('What is your current installment rate as a percentage of disposable income',1,4)
            submit_text = st.form_submit_button(label='Submit')
            feature_list = [get_value(Foreign_worker, worker_dict),get_value(Gender, gender_dict),get_value(Status,status),get_value(Credit_Hist,credit_history), get_value(SvgBond, savings_account_bond), 
                            get_value(InstallmentRate,installmentRate),get_value(DebtGuarantors,debtorsGuarantors), get_value(PropertyValue, property_dict), get_value(otherInstallmentPlans,other_installment_plans), 
                            get_value(Housing,housing), Age, CreditAmount, InstallmentRateIncome, Duration]
            st.write(feature_list)
            pretty_results = {'Foreign_worker': Foreign_worker, "Gender":Gender, "Status":Status, "Credit_Hist":Credit_Hist, "SvgBond":SvgBond, "InstallmentRate":InstallmentRate,
                            "DebtGuarantors": DebtGuarantors, "PropertyValue":PropertyValue, "otherInstallmentPlans":otherInstallmentPlans, "Housing":Housing, "Duration":Duration, "Age":Age,
                            "CreditAmount":CreditAmount, "InstallmentRateIncome":InstallmentRateIncome}
            st.info(tuple(pretty_results.values()))
            single_sample = np.array(feature_list).reshape(1, -1)
            
        #ML
            if submit_text:
                loaded_model = load_model("model/credit_score.pkl")
                pred_prob = loaded_model.predict_proba(single_sample)
                prediction = loaded_model.predict(single_sample)
                add_prediction(Foreign_worker, Gender, Status, Credit_Hist, SvgBond, InstallmentRate, DebtGuarantors,PropertyValue, Age,otherInstallmentPlans, Housing, Duration, InstallmentRateIncome, CreditAmount)
                
                if prediction == 1:
                    st.success('Huuray you have a good score')
                    pred_probability = {'Good':pred_prob[0][1]*100, 'Bad':pred_prob[0][0]*100}
                    st.subheader('Prediction Probability Score')
                    st.json(pred_probability)
                else:
                    st.warning('Sorry you have a bad score')
                    pred_probability = {'Good':pred_prob[0][0]*100, 'Bad':pred_prob[0][1]*100}
                    st.subheader('Prediction Probability Score')
                    st.json(pred_probability)

    elif choice == "Monitor":
        add_data('Monitor', datetime.now())
        st.subheader('Result Monitoring for the application')
        with st.expander('Page Metrics'):
            page_visit_details = pd.DataFrame(view_data(), columns = ['Pagename', 'Time_of_Visit'])
            st.dataframe(page_visit_details)
            pg_count = page_visit_details['Pagename'].value_counts().rename_axis('Pagename').reset_index(name='Counts')
            c = alt.Chart(pg_count).mark_bar().encode(x = 'Pagename', y = 'Counts', color = 'Pagename')
            st.altair_chart(c, use_container_width=True)
            
            p = px.pie(pg_count, values = 'Counts', names = 'Pagename')
            st.plotly_chart(p, use_container_width=True)
        with st.expander('Predictions'):
            customer_detail = pd.DataFrame(view_all_data(), columns=['Foreign_worker', 'Gender', 'Status', 'Credit_Hist', 'SvgBond', 'InstallmentRate',  'DebtGuarantors', 'PropertyValue', 'Age',
                                            'otherInstallmentPlans', 'Housing', 'Duration','InstallmentRateIncome', 'CreditAmount'])
            st.dataframe(customer_detail)  
            #custom group by function     
        #with st.expander('Visualizations'):
        #    score_dist = customer_detail.groupby('Score').count()
        #    p= px.histogram(score_dist)                                               
        #    st.plotly_chart(p,use_container_width=True )
        
    else:
        st.subheader("About")
        add_data('About', datetime.now())
        st.write('Here we look at what it takes to have a good credit scoring')
      



if __name__ == '__main__':
    main()