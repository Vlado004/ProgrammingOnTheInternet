import database
import os
from http import cookies

def getSession():
    httpCookie = os.environ.get('HTTP_COOKIE', '')
    cookieObject = cookies.SimpleCookie(httpCookie)
    session_id = cookieObject.get("session_id").value if cookieObject.get("session_id") else None
    if session_id is None:
        session_id = database.createSession()
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = session_id
        print (cookies_object.output())
    return session_id


def addSession(parameters):
    session_id = getSession()
    data = database.getSession(session_id)
    for course in parameters.keys():
        data[course] = parameters.getvalue(course)
    database.replaceSession(session_id, data)

def getData():
    session_id = getSession()
    data = database.getSession(session_id)
    return data
