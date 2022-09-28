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
import os 
from manage_db import *
#def load_model(model_file):
import joblib

# track utilities
# feature columns for the predictions
SelectedColumns = ['Foreign_Worker',
 'Sex',
 'Status',
 'Credit history',
 'Saving_acccount_bonds',
 'Installment_Rate',
 'Debtors_Guarantors',
 'Property',
 'Other_Installment_Plans',
 'Housing','Duration', 'Age', 'Credit_Amount', 'Installment_Rate/Income']

data = pd.read_csv('case_hepster_clean.csv')
def load_model(model_file):
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
        Foreign_worker = st.selectbox('Are you a foreign worker?', ('Yes', 'No'))
        Gender = st.selectbox('What is your Gender ?', ('Male', 'Female'))
        status = data['Status'].unique()
        Status = st.selectbox('What is the status of your checking account?', status)
        credit_hist = data['Credit history'].unique()
        Credit_Hist = st.selectbox('Which text best describes your credit history', credit_hist)
        svg_bond = data['Saving_acccount_bonds']
        SvgBond = st.selectbox('Do you have a savings account or a Bond?', svg_bond)
        installRate = data['Installment_Rate'].unique()
        InstallmentRate = st.selectbox('What is your current installment rate ?', installRate)
        debtguarantors = data['Debtors_Guarantors'].unique()
        DebtGuarantors = st.selectbox('Indicate if you have a guarantor Status', debtguarantors)
        propertyValue = data['Property'].unique()
        PropertyValue = st.selectbox('Indicate your current property', propertyValue)
        other = data['Other_Installment_Plans'].unique()
        otherInstallmentPlans = st.selectbox('Do you have other installment plans', other)
        housing = data['Housing'].unique()
        Housing = st.selectbox('What is your housing status', housing)
        Age = st.number_input('Indicate your age', 18 , 90)
        CreditAmount = st.number_input('Indicate your Credit Amount')
        installmentRate_income = data['Installment_Rate/Income'].sort_values().unique()
        InstallmentRateIncome = st.selectbox('What is your current installment rate as a percentage of disposable income', installmentRate_income)
    




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
            customer_detail = pd.DataFrame(view_all_data(), columns=['ID', 'Status', 'Duration', 'Credit history', 'Purpose',
                                                                    'Credit_Amount', 'Saving_acccount_bonds', 'Installment_Rate',
                                                                    'Installment_Rate/Income', 'Personal status and sex',
                                                                    'Debtors_Guarantors', 'Resident_Years', 'Property', 'Age',
                                                                    'Other_Installment_Plans', 'Housing', 'No_Credits', 'Job', 'Dependents',
                                                                    'Telephone', 'Foreign_Worker', 'Score'])
            st.dataframe(customer_detail)  
            #custom group by function     
        with st.expander('Visualizations'):
            score_dist = customer_detail.groupby('Score').count()
            p= px.histogram(score_dist)                                               
            st.plotly_chart(p,use_container_width=True )
        
    else:
        st.subheader("About")
        st.write('Here we look at what it takes to have a good credit scoring')
        #add_data('About', datetime.now())



if __name__ == '__main__':
    main()