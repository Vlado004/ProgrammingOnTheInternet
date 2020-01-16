import database
import os
from http import cookies
import time
from datetime import datetime

def createSession(user):
    session_id = database.createSession(user)
    cookies_object = cookies.SimpleCookie()
    cookies_object["session_id"] = session_id
    print (cookies_object.output())

def destroySession():
    session_id = getSessionID()
    destroySessionID()
    database.destroySession(session_id)

def getSessionID():
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    session_id = get_all_cookies_object.get("session_id").value if get_all_cookies_object.get("session_id") else None
    return session_id

def destroySessionID():
    cookies_object = cookies.SimpleCookie()
    cookies_object["session_id"] = ""
    cookies_object["session_id"]["expires"] = 'Thu, 01 Jan 1970 00:00:00 GMT'
    print (cookies_object.output())

def getCurrCollection():
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    collection_id = get_all_cookies_object.get("collection_id").value if get_all_cookies_object.get("collection_id") else None
    return collection_id

def setCollection(collectionID):
    cookies_object = cookies.SimpleCookie()
    cookies_object["collection_id"] = collectionID
    print (cookies_object.output())

def createCookieCounter(image_id):
    cookies_object = cookies.SimpleCookie()
    cookies_object["image_id_" + str(image_id)] = 1
    end = time.gmtime(time.time() + 365.25 * 24 * 3600)
    expires = time.strftime("%a, %d-%b-%Y %T GMT", end)
    cookies_object["image_id_" + str(image_id)]["expires"] = expires
    return cookies_object

def createCounterCookie(image_id):
    cookies_object = cookies.SimpleCookie()
    cookies_object["image_id_" + str(image_id)] = image_id
    cookies_object["last_visited_" + str(image_id)] = datetime.now()
    cookies_object["image_id_" + str(image_id)]['expires'] = 365 * 24 * 3600
    cookies_object["last_visited_" + str(image_id)]['expires'] = 24 * 3600
    print(cookies_object.output())

def checkIfCounted(image_id):
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    cookie = cookies.SimpleCookie(http_cookies_str)
    if cookie.get("image_id_" + str(image_id)):
        if not cookie.get("last_visited_" + str(image_id)):
            cookie["last_visited_" + str(image_id)] = datetime.now()
            cookie["last_visited_" + str(image_id)]['expires'] = 24 * 3600
            print(cookie.output())
            return True
        return False
    else:
        createCounterCookie(image_id)
        return True
