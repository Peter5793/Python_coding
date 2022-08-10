"""
analysis of Twitter feeds for sentiment analysis
"""
#importing the necesary libraries

#pip install -U scikit-learn
#pip install nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

import nltk
import re
import string
from nltk.stem import WordNetLemmatizer
import pandas as pd



# reading the data
test_csv = pd.read_csv('test_data (1).csv')
test_csv.head()
=======
train_csv = pd.read_csv('C:/Users/')

train_csv.head()
train_csv.iloc[0,0]

# stopwoards removal and lemmatization
stopwords = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()

#downloading the stopwords
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

train_csv.columns
names = ['review', 'outcome']
train_csv.columns = names
train_csv.head()
test_csv.columns = names

#splitting the data
train_x = train_csv['review']
train_y = train_csv ['outcome']
test_x = test_csv['review']
test_y = test_csv['outcome']

# making empty list that will be appended we pre-processed data

train_X = []
test_X = []
for i in range(0, len(train_x)):
    review = re.sub('[^a-zA-Z]', ' ', train_x[i])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if not word in set(stopwords)]
    review = ''.join(review)
    train_X.append(review)
    
    
for i in range(0, len(test_x)):
    review = re.sub('[^a-zA-Z]', ' ', test_x[i])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if not word in set(stopwords)]
    review = ''.join(review)
    test_X.append(review)
    
train_X[10]

# intialize a tfidf object
tf_idf = TfidfVectorizer()
# applying the tfidf to the trainig data
x_train_df = tf_idf.fit_transform(
    train_X)
x_train_df = tf_idf.transform(train_X)

print('n_smaples {}, features: {}', format(x_train_df.shape))

# transforming the test data into a tfidf matrix
X_test_tf  = tf_idf.transform(test_X)

print('n_smaples {}, features: {}', format(X_test_tf.shape))

# using naives bayes classifier
naives_bayes_classifier = MultinomialNB()
naives_bayes_classifier.fit(x_train_df, train_y)

y_pred = naives_bayes_classifier.predict(X_test_tf)

print(metrics.classification_report(test_y, y_pred, target_names = ['Positive', 'Negative']))
print('Confusion Matrix')
print(metrics.confusion_matrix(test_y, y_pred))





#Prediction trials
test = ['i enjoyed really good']
review = re.sub('[^a-zA-Z]', '', test[0])
review = review.lower()
review = review.split()
review = [lemmatizer.lemmatize(word) for word in review if not word in set(stopwords)]
test_processed = [''.join(review)]

test_processed

test_input = tf_idf.transform(test_processed)

test_input.shape

#place sample through bayes
res = naives_bayes_classifier.predict(test_input)[0]
if res == 1:
    print('positive review')
elif res ==0:
    print('negative review')
