#!C:\Users\Mateo\AppData\Local\Programs\Python\Python38\python.exe

import html_base
import database
import authentication
import cgi
import os
import session

session_id = session.getSessionID()
if session_id is None:
    print("Location: login.py")

success = True
if os.environ["REQUEST_METHOD"].upper() == "POST":
    parameters = cgi.FieldStorage()
    usr = database.getUserIDViaSessionID(session_id)[0]
    usrData = database.getUserData(usr)
    old_pw = parameters.getvalue("old_pw")
    pw1 = parameters.getvalue("pw1")
    pw2 = parameters.getvalue("pw2")

    if authentication.authenticate(usrData[1], old_pw)[0] is False:
        success = False
    elif pw1 != pw2:
        success = False

    if success:
        authentication.changePassword(usrData[0], pw1)
        session.destroySession()
        print("Location: login.py")


html_base.start()

print("""
    <form method="POST">
        Old password: <input type="password" name="old_pw" /><br/>
        New password: <input type="password" name="pw1" /><br/>
        Re-enter new password: <input type="password" name="pw2" /><br/>

        <input type="submit" value="Change" />
    </form>

    <a href="login.py">Login</a>
""")

if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>Password change Error!</div>")

html_base.end()
