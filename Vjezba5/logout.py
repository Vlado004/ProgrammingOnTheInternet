#!C:\Users\Mateo\AppData\Local\Programs\Python\Python38\python.exe

import html_base
import session

session_id = session.getSessionID()
if session_id is None:
    print("Location: login.py")

session.destroySession()
print ("Location: login.py")
print("")

html_base.start()
html_base.end()
