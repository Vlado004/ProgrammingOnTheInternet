#!C:\Users\Mateo\AppData\Local\Programs\Python\Python38\python.exe

import html_base
import database
import authentication
import cgi
import os

success = True
if os.environ["REQUEST_METHOD"].upper() == "POST":
    parameters = cgi.FieldStorage()
    usr = parameters.getvalue("username")
    email = parameters.getvalue("email")
    pw1 = parameters.getvalue("pw1")
    pw2 = parameters.getvalue("pw2")

    if database.checkIfEmailIsUsed(email):
        success = False
    elif database.getUserIDViaUserName(usr):
        success = False
    elif pw1 != pw2:
        success = False

    if success:
        authentication.register(usr, email, pw1)
        print("Location: login.py")

html_base.start()

print("""
    <form method="POST">
        Username: <input type="text" name="username" /><br/>
        Email: <input type="email" name="email" /><br/>
        Password: <input type="password" name="pw1" /><br/>
        Re-enter password: <input type="password" name="pw2" /><br/>

        <input type="submit" value="Register" />
    </form>

    <a href="login.py">Login</a>
""")

if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("<div>Registration Error!</div>")

html_base.end()
