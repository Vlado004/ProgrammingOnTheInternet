import mysql.connector
from datetime import datetime

def connect():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        database="test",
    )
    return db

def createSession(user):
    mydb = connect()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO session (user_id) VALUES (" + str(user) + ")")
    mydb.commit()
    return cursor.lastrowid

def destroySession(sessionID):
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM session WHERE session_id = '" + str(sessionID) + "'")
    db.commit()

def getImagesViaCollectionID(collection_id):
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM image WHERE collection_id='" + str(collection_id) + "'")
    result = cursor.fetchall()
    return result

def getImageViaImageID(image_id):
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM image WHERE image_id='" + str(image_id) + "'")
    return cursor.fetchone()

def getImages():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM image")
    return cursor.fetchall()

def getCollectionIDs():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM collections")
    result = cursor.fetchall()
    return result

def createCollection(collectionName):
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO collections (name) VALUES ('" + collectionName + "')")
    db.commit()

def uploadImage(image, collection_id):
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO image (name, collection_id) VALUES ('" + image.filename + "', '" + str(collection_id) + "')")
    db.commit()

def deleteImage(image_id):
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM image where image_id='" + str(image_id) + "'")
    db.commit()

def incrementImageCounter(image_id):
    db = connect()
    cursor = db.cursor()
    cursor.execute("UPDATE image SET counter = counter + 1, last='" + str(datetime.now()) + "' WHERE image_id='" + str(image_id) + "'")
    db.commit()

def createUser(username, email, password):
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    values = (username, email, password)
    db = connect()
    cursor = db.cursor()
    try:
        cursor.execute(query, values)
        db.commit()
    except:
        return False
    return True

def changePassword(user_id, password):
    db = connect()
    cursor = db.cursor()
    values = (password,)
    query = "UPDATE users SET password=%s WHERE user_id = '" + str(user_id) + "'"
    cursor.execute(query, values)
    db.commit()

def getUserIDViaUserName(username):
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT user_id FROM users WHERE username = '" + username + "'")
    return cursor.fetchone()

def getUserIDViaSessionID(session_id):
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT user_id FROM session WHERE session_id = '" + str(session_id) + "'")
    return cursor.fetchone()

def getUserRoleViaSessionID(session_id):
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT role FROM users INNER JOIN session ON users.user_id=session.user_id WHERE session_id='" + session_id + "'")
    return cursor.fetchone()

def getUserData(user_id):
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = '" + str(user_id) + "'")
    return cursor.fetchone()

def checkIfEmailIsUsed(email):
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = '" + email + "'")
    if cursor.fetchone() is None:
        return False
    return True
