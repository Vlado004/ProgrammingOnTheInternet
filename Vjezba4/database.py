import mysql.connector
import json

def connect():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        database="test",
    )
    return db

def createSession():
    query = "INSERT INTO vj4 (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = connect()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid

def getSession(session_id):
    mydb = connect()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM vj4 WHERE session_id=" + str(session_id))
    rows = cursor.fetchone()
    return json.loads(rows[1])

def replaceSession(session_id, data):
    mydb = connect()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO vj4(session_id,data)
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()
