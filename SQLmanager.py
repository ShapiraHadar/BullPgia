import mysql.connector

def connect():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="bull_pgia",
        )
    except mysql.connector.Error as err:
        print("failed to connect to sql")
        exit(1)
    return mydb

def add_history(db, secret, attempts):
    cursor = db.cursor()
    cursor.execute(f"insert into history values ('{attempts}', '{secret}')")
    db.commit()

def minimum_attempt(db):
    cursor = db.cursor()
    cursor.execute("(select min(attempts) from history)")
    return cursor.fetchone()[0]
