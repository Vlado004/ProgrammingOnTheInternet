#!C:\Users\Mateo\AppData\Local\Programs\Python\Python38\python.exe

import database
import bcrypt

def register(username, email, password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return database.createUser(username, email, hashed)

def authenticate(username, password):
    user = database.getUserIDViaUserName(username)
    if (user):
        userData = database.getUserData(user[0])
        if(bcrypt.checkpw(password.encode('utf-8'), userData[3].encode('utf-8'))):
            return True, user[0]
        else:
            return False, None
    else:
        return False, None

def changePassword(username, password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return database.changePassword(username,hashed)
