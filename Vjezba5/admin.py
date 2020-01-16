#!C:\Users\Mateo\AppData\Local\Programs\Python\Python38\python.exe

import html_base
import database
import session
import os
import cgi

session_id = session.getSessionID()
if session_id is None:
    print("Location: login.py")
else:
    user_role = database.getUserRoleViaSessionID(session_id)[0]
    if user_role != "admin":
        print("Location: index.py")

html_base.start()

images = database.getImages()
for img in images:
    print("<b>Image:</b> " + img[1] + ", <b>Clicks:</b> " + str(img[5]) + ", <b>Last clicked:</b> " + str(img[4]) + "<br/>")

print('<br/><a href="index.py">Return</a>')

html_base.end()
