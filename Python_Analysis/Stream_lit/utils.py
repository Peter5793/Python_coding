# load database packages
import sqlite3
from xml.sax.handler import feature_external_ges
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

# functions
def page_visit():
    c.execute('CREATE TABLE IF NOT EXISTS tracker (pagename TEXT, timeofvisit TIMESTAMP)')

def add_data(pagename, timeofvisit):
    c.execute('INSERT INTO tracker(pagename, timeofvisit) VALUES (?,?)', (pagename, timeofvisit))
    conn.commit()
#
def view_data():
#    """ view page vist data"""
   c.execute('SELECT * FROM tracker')
   data = c.fetchall()
   return data

# track input and prediction
def track_review():
    c.execute('CREATE TABLE IF NOT EXISTS review_table(rawtext TEXT, prediction TEXT, probability NUMBER, timeofvisit TIMESTAMP)')
    conn.commit()

def add_prediction(rawtext, prediction, probability, timeofvisit):
    c.execute('INSERT INTO review_table(rawtext, prediction, probability, timeofvisit) VALUES(?,?,?,?)',(rawtext, prediction, probability, timeofvisit))
    conn.commit()

def view_all_data():
    c.execute('SELECT * FROM review_table')
    data = c.fetchall()
    return data