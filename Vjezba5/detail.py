#!C:/Users/Mateo/AppData/Local/Programs/Python/Python38/python.exe

import html_base
import database
import session
import os
import cgi

session_id = session.getSessionID()
if session_id is None:
    print("Location: login.py")

parameters = cgi.FieldStorage()
image_id = parameters.getvalue("image_id")
image_info = database.getImageViaImageID(image_id)

if os.environ["REQUEST_METHOD"].upper() == "POST":
    database.deleteImage(image_id)
    os.remove("D:/Programs/htdocs/scripts/image/" + image_info[1])
    print("Location: index.py")
else:
    if session.checkIfCounted(image_id):
        database.incrementImageCounter(image_id)

html_base.start()

print('<img src="image/' + image_info[1] + '" alt="' + str(image_info[0]) + '"><br/>')
print('<a href="index.py">Return</a><br/>')
print('<form method="POST"><input type="submit" value="Delete :)"></form>')

html_base.end()
