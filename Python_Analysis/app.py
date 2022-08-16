# import packages
from dataclasses import replace
from venv import create
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import streamlit as st

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import train_test_split

import nltk
import re
import string
from nltk.stem import WordNetLemmatizer
import pandas as pd

import sqlite3
conn = sqlite3.connect('data_2.db')
c= conn.cursor()

#downloading the stopwords
#nltk.download('stopwords')
#nltk.download('wordnet')
#nltk.download('omw-1.4')

# stopwoards removal and lemmatization
stopwords = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def create_table():
    """ Create table in SQL lite"""
    c.execute('CREATE TABLE IF NOT EXISTS Movie_Review ( post_date DATE, comment TEXT, result TEXT)')

def view_data():
    """ observe all the data"""
    c.execute('SELECT * FROM Movie_Review')
    data = c.fetchall()
    return data

def add_data(post_date, comment, result):
    """ add new data to the library"""
    c.execute('INSERT INTO Movie_Review (ID, comment , result) VALUES (?,?,?)',(post_date, comment, result))
    conn.commit()

# import dataset
data = pd.read_csv('train_data (1).csv')
data_2 = data.apply(tuple, axis = 1)
print(data_2)


column_name = ['review', 'answer']
data.columns = column_name

data['answer'] = data['answer'].replace(0, 'negative')
data['answer'] = data['answer'].replace(1, 'positive')
#  preprocessing of the information

# converting the text  to lowercase
data['review'] = data['review'].apply(str.lower)
# using regex to remove punctuation 
data['review'] = data['review'].apply(lambda x: re.sub(r'[^\w\s]', '', x ))
# removing stopwords
data['review'] = data['review'].apply(lambda x : ''.join( w for w in x.split() if w not in stopwords))

# creation a lemamtizer object
lemmatizer = WordNetLemmatizer()
def lemmatize_words(text):
    """ lemmatize words in the text"""
    words = text.split()
    words = [lemmatizer.lemmatize(word, pos='v') for word in words]
    return ''.join(words)
data['review'] = data['review'].apply(lemmatize_words)

# split train and test the data
train_x = data.iloc[:, 0]
train_y = data.iloc[:, 1]

train_X, test_X, train_Y, test_Y = train_test_split(train_x, train_y, random_state=42, test_size=0.2, shuffle=True)

print('size of train x : {}, y : {}'.format(train_X.shape, train_Y.shape))
print('size of test x : {}, y : {}'.format(test_X.shape, test_Y.shape))
#TODO build logisti cregression pipline
#TODO train and fit
#TODO check accuracy
# initialize TFIDF vectorizer
tf_idf = TfidfVectorizer()
# creat a naive baiyes classifier


# applying the tfidf to the trainig data
x_train_df = tf_idf.fit_transform(train_x)
x_train_df = tf_idf.transform(train_x)
X_test_tf  = tf_idf.transform(test_Y)

print('n_samples {}, features: {}', format(x_train_df.shape))



# using naives bayes classifier
nbc = MultinomialNB()
nbc.fit(x_train_df, train_y)

y_pred = nbc.predict(X_test_tf)

print(metrics.classification_report(test_Y, y_pred, target_names = ['Positive', 'Negative']))
print('Confusion Matrix')
print(metrics.confusion_matrix(test_Y, y_pred))

def main():
    Menu = ['Home', 'Manage', 'About']
    create_table()
    choice = st.sidebar.selectbox('Menu', Menu)
    if choice == 'Home':
        st.subheader('Home')
        with st.form(key = "Ml Form"):
            col1, col2 = st.columns([3, 2])
            with col1:
                message = st.text_area("Movie Review Comment")
                submit_message = st.form_submit_button(label='Classify')
            with col2:
                st.write("Review movie comments using Naive-Bayes Classification")
    elif choice == "Manage":
        st.subheader("Manage & Monitor")
        stored_data = view_data()
               


if __name__ == "__main__":
    main()


