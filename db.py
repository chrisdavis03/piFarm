import sqlite3

def createVOTR():
    conn = sqlite3.connect('piplant.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE topics
                 (id INT PRIMARY KEY, name TEXT NOT NULL)''')

    c.execute('''CREATE TABLE options
                     (id INT PRIMARY KEY, name TEXT NOT NULL)''')

    c.execute('''CREATE TABLE polls
                     (id INT PRIMARY KEY, topic_id INT, option_id INT, 
                     FOREIGN KEY(topic_id) REFERENCES topics(id),
                     FOREIGN KEY(option_id) REFERENCES options(id))''')

    c.execute('''CREATE TABLE users
                         (id INT PRIMARY KEY, email VARCHAR(100) UNIQUE, user VARCHAR(50),
                         password VARCHAR(200))''')

    conn.commit()
    conn.close()

def votr_UserSignup(email, username, password):
    conn = sqlite3.connect('piplant.db')
    c = conn.cursor()

    #todo - currently, we can signup users with identical credentials. Maybe change username to be UNIQUE?
    #todo - handle failures in SQL

    try:
        c.execute('''INSERT INTO users (email, user, password)VALUES
                         (?, ?, ? )''', (email, username, password))
        error = 0
    except:
        error = 1
    conn.commit()
    conn.close()
    return error

def votr_Userlookup(email):
    conn = sqlite3.connect('piplant.db')
    c = conn.cursor()

    c.execute('''SELECT user, password FROM users WHERE email = (?)''',[email])
    user = c.fetchall()

    conn.close()
    return user[0][0], user[0][1]
if __name__ == "__main__":
    #createVOTR()
    pass
