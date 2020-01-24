import sqlite3



def status():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM lights_schedule")
    schedule = c.fetchall()
    print(schedule)

def columns():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM lights_schedule")
    columns = c.description[0]
    print(columns)


def getzone1():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM lights_schedule WHERE zone_id=1")
    zone = c.fetchall()

    conn.close()

    startTime = zone[0][1]
    endTime = zone[0][2]

    return zone, startTime, endTime