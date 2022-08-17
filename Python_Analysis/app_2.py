# core packages
from tkinter.font import names
from turtle import color
from unittest import result
from venv import create
import streamlit as st
import altair as alt
import plotly.express as px

#import EDA pkgs
import pandas as pd
import numpy as np
from datetime import datetime

# utility files
import joblib
pipe_lr = joblib.load(open("movie_classifier_2022.pkl", "rb"))

# track utilities
from utils import view_all_data,  track_review, add_data, add_prediction, page_visit, view_data

def predict_review(docx):
    """ predict the review from use input"""
    result = pipe_lr.predict([docx])
    return result[0]

def predictions_proba(docx):
    """ Probability of the user input on whether it is positive or negative
    """
    result = pipe_lr.predict_proba([docx])
    return result

# output dictionary
review_dict = {'positive': '❤', 'negative': '💔'}

def main():
    st.title("Movie Review Classifier")
    Menu = ["Home", "Monitor", "About"]
    choice = st.sidebar.selectbox("Menu", Menu)
    page_visit()
    track_review()
    if choice == "Home":
        add_data("Home", datetime.now())
        st.subheader("Movie Review in Text")

        with st.form(key = 'movie_form'):
            raw_text = st.text_area('Give your movie review here')
            submit_text = st.form_submit_button(label='Submit')
        
        if submit_text:
            col1, col2 = st.columns(2)
            prediction = predict_review(raw_text)
            probability = predictions_proba(raw_text)

            add_prediction(raw_text, prediction, np.max(probability), datetime.now())

            with col1:
                st.success('Original text')
                st.write(raw_text)
                st.success('Prediction')
                icon = review_dict[prediction]
                st.write("{}:{}".format(prediction, icon))
                st.write("Confidence: {}".format(round(np.max(probability),2)))

            with col2:
                st.success('Prediction probability')
                prob_df = pd.DataFrame(probability, columns=pipe_lr.classes_)
                prob_df_clean = prob_df.T.reset_index()
                prob_df_clean.columns = ["Review", "Probability"]

                fig = px.bar(prob_df_clean, x = 'Review', y = 'Probability', color='Review', title= 'Movie Review Chart')
                st.plotly_chart(fig, use_container_width=True)

    elif choice == 'Monitor':
        add_data("Monitor", datetime.now())
        st.subheader('Monitor Application')
        with st.expander('Page Metrics'):
            page_visit_details = pd.DataFrame(view_data(), columns=['Pagename', 'Time of Visit'])
            st.dataframe(page_visit_details)

            pg_count = page_visit_details['Pagename'].value_counts().rename_axis('Pagename').reset_index(name='Counts')
            c = alt.Chart(pg_count).mark_bar().encode(x = 'Pagename', y = 'Counts', color = 'Pagename')
            st.altair_chart(c, use_container_width=True)
            
            p = px.pie(pg_count, values = 'Counts', names = 'Pagename')
            st.plotly_chart(p, use_container_width=True)
    
    else:
        st.subheader("About")
        st.write('How does a review look like for a Movie')
        add_data('About', datetime.now())


if __name__ == '__main__':
    main()