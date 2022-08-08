import sqlite3
conn = sqlite3.connect('data.db')
c= conn.cursor()
# connects to SQlite3 database where all the dat awill be stored
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