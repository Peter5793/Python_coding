# import custom functions
from tables import *
# core packages 
from audioop import add
from email import message
from tkinter import Menu
from turtle import position
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import altair as alt
import plotly.express as px
import dash
# Online Ml Packages
from river.naive_bayes import MultinomialNB
from river.feature_extraction import BagOfWords, TFIDF
from river.compose import Pipeline

# training data
data = [("my unit test failed","software"),
("tried the program, but it was buggy","software"),
("i need a new power supply","hardware"),
("the drive has a 2TB capacity","hardware"),
("unit-tests","software"),
("program","software"),
("power supply","hardware"),
("drive","hardware"),
("it needs more memory","hardware"),
("check the API","software"),
("design the API","software"),
("they need more CPU","hardware"),
("code","software"),
("i found some bugs in the code","software"),
("i swapped the memory","hardware"),
("i tested the code","software"),
("monitor","hardware"),
("processing units","hardware")]


model = Pipeline(('vectorizer', TFIDF(lowercase=True)), ('nv', MultinomialNB()))
for x, y in data:
    model = model.learn_one(x, y)

#storage in database
import sqlite3
conn = sqlite3.connect('data.db')
c= conn.cursor()

# create table
def create_table():
    """ function that creates table in SQl"""
    c.execute('CREATE TABLE IF NOT EXISTS Prediction_Table(message TEXT, prediction TEXT, probability NUMBER, software_prob NUMBER, hardware_prob NUMBER, post_date DATE)')

def add_data(message, prediction , probability, software_prob, hardware_prob, post_date):
    """ Add data into the SQL Table"""
    c.execute('INSERT INTO Prediction_Table(message, prediction , probability, software_prob, hardware_prob, post_date) VALUES (?,?,?,?,?,?)',(message, prediction , probability, software_prob, hardware_prob, post_date))
    conn.commit()

def view_data():
    """ Create a UI for the user to look at the data that has been inputed"""
    c.execute('SELECT * FROM Prediction_Table')
    data = c.fetchall()
    return data


def main():
    """ Main function that creates the side bar menu and  visualizes the parameters from the other functions"""
    Menu = ["Home", "Manage", "About"]
    create_table()
    choice = st.sidebar.selectbox("Menu", Menu)
    if choice == "Home":
        st.subheader('Home')
        with st.form(key = "Ml Form"):
            col1, col2 = st.columns([3, 2])
            with col1:
                message = st.text_area("Message")
                submit_message = st.form_submit_button(label='Predict')
            with col2:
                st.write("Online Incremental ML")
                st.write("Predict input as Software or hardware")
        if submit_message:
            prediction = model.predict_one(message)
            prediction_prob = model.predict_proba_one(message)
            probability = max(prediction_prob.values())
            postdate = datetime.now()
            # add data to the database
            add_data(message, prediction, probability, prediction_prob['software'], prediction_prob['hardware'], postdate)
            st.success("Input Submiited")


            res_col1, rescol2 = st.columns(2)
            with res_col1:
                st.info('Original Text')
                st.write(message)

                st.success("Your Prediction")
                st.write(prediction)

            with rescol2:
                st.info("Probability")
                st.write(prediction_prob)

            # plotting
            df = pd.DataFrame({'label':prediction_prob.keys(), 'Probability': prediction_prob.values()})
            #st.dataframe(df)
            #visualization
            fig = alt.Chart(df).mark_bar().encode(x='label', y = 'Probability')
            st.altair_chart(fig, use_container_width=True)

    elif choice == "Manage":
        st.subheader("Manage & Monitor")
        stored_data = view_data()
        new_df = pd.DataFrame(stored_data, columns=['message', 'prediction' , 'probability', 'software_prob', 'hardware_prob', 'post_date'])
        st.dataframe(new_df)
        
        new_df['post_date'] = pd.to_datetime(new_df["post_date"])
        c = alt.Chart(new_df).mark_line().encode(x= 'post_date', y = 'probability')
        c = alt.Chart(new_df).mark_line().encode(x= 'minutes(post_date)', y = 'probability')
        st.altair_chart(c)
        try:
            c_hard = alt.Chart(new_df['hardware_prob'].reset_index()).mark_line().encode(x= 'hardware_prob', y = 'index')
            c_soft = alt.Chart(new_df['software_prob'].reset_index()).mark_line().encode(x= 'software_prob', y = 'index')
            
            c1, c2 = st.columns(2)
            with c1:
                with st.expander('Hardware Probability'):
                    st.altair_chart(c_hard, use_container_width= True)
            with c2:
                with st.expander('Software Probability'):
                    st.altair_chart(c_soft, use_container_width=True)
            
        except:
            st.info('No data can Plotted')    
                
    else:
        #TODO add a fucntion that brings the about page
        st.subheader("About")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('Name')
            st.write('This is a project on Incremental Machine Learning')
        with col2:
            st.subheader('Description')
            st.write('What tto expect')
       

        

if __name__ == '__main__':
    main()