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
    c.execute('CREATE TABLE IF NOT EXISTS review('
        'Name TEXT, Status TEXT, Duration INT, Purpose TEXT, Credit_Amount INT, Saving_acccount_bonds TEXT,'
        'Installment_Rate TEXT, Installment_Rate_Income INT, Debtors_Guarantors TEXT, Resident_Years INT,'
        'Property TEXT, Age INT, Other_Installment_Plans TEXT, Housing TEXT, No_Credits INT, Job TEXT, Dependents INT,'
        'Telephone TEXT, Foreign_Worker TEXT, Score)')
    conn.commit()

def add_prediction(Name, Status, Duration , Purpose , Credit_Amount , Saving_acccount_bonds,
        Installment_Rate, Installment_Rate_Income, Debtors_Guarantors , Resident_Years,
        Property, Age, Other_Installment_Plans, Housing , No_Credits, Job,Dependents,
        Telephone , Foreign_Worker, Score):
        c.execute('INSERT INTO review ( Name, Status, Duration , Purpose , Credit_Amount , Saving_acccount_bonds,'
        'Installment_Rate, Installment_Rate_Income, Debtors_Guarantors , Resident_Years,'
        'Property, Age, Other_Installment_Plans, Housing , No_Credits, Job,Dependents,'
        'Telephone , Foreign_Worker, Score) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (Name, Status, Duration , Purpose , Credit_Amount , Saving_acccount_bonds,
        Installment_Rate, Installment_Rate_Income, Debtors_Guarantors , Resident_Years,
        Property, Age, Other_Installment_Plans, Housing , No_Credits, Job,Dependents,
        Telephone , Foreign_Worker, Score))

def view_all_data():
    c.execute('SELECT * FROM review')
    data = c.fetchall()
    return data

# track the input and the prediction