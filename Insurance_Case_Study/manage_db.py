import sqlite3
conn = sqlite3.connect('usedata.db', check_same_thread=False)
c = conn.cursor()

# functions
def page_visit():
    c.execute('CREATE TABLE IF NOT EXISTS tracker (pagename TEXT, timeofvisit TIMESTAMP)')

def add_data(pagename, timeofvisit):
    c.execute('INSERT INTO tracker (pagename, timeofvisit) VALUES (?,?)', (pagename, timeofvisit))
    conn.commit()

def view_data():
    c.execute('SELECT * FROM tracker')
    data = c.fetchall()
    return data 


def track_review():
    c.execute('CREATE TABLE IF NOT EXISTS review (Foreign_worker TEXT, Gender VARCHAR(256), Status TEXT, Credit_History TEXT, Saving_acccount_bonds TEXT,Installment_Rate TEXT,  Debtors_Guarantors TEXT, Property TEXT, Age INT, Other_Installment_Plans TEXT, Housing TEXT,Duration INT,Installment_Rate_Income INT,Credit_Amount)')
    conn.commit()

def add_prediction(Foreign_worker, Gender, Status,  Credit_History, Saving_acccount_bonds,Installment_Rate,  Debtors_Guarantors, Property,Age, Other_Installment_Plans, Housing, Duration,Installment_Rate_Income,Credit_Amount):
    c.execute('INSERT INTO review (Foreign_worker, Gender, Status,  Credit_History, Saving_acccount_bonds,Installment_Rate,  Debtors_Guarantors, Property,Age, Other_Installment_Plans, Housing, Duration,Installment_Rate_Income, Credit_Amount)'
     'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Foreign_worker, Gender, Status,  Credit_History, Saving_acccount_bonds,Installment_Rate,  Debtors_Guarantors, Property,Age, Other_Installment_Plans, Housing, Duration,Installment_Rate_Income, Credit_Amount))
    conn.commit()

def view_all_data():
    c.execute('SELECT * FROM review')
    data = c.fetchall()
    return data

# track the input and the prediction