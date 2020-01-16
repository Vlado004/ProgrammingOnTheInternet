#!C:\Users\Mateo\AppData\Local\Programs\Python\Python38\python.exe

import html_base
import cgi
import os
import authentication
import session

success = True
if os.environ["REQUEST_METHOD"].upper() == "POST":
    success = False
    parameters = cgi.FieldStorage()
    usr = parameters.getvalue("username")
    pwd = parameters.getvalue("pwd")
    result = authentication.authenticate(usr, pwd)
    if result[0] == True:
        #login sranja - sesija i to
        success = True
        session.createSession(result[1])
        print("Location: index.py")



html_base.start()

print("""
    <form method="POST">
        Username: <input type="text" name="username" /> <br/>
        Password: <input type="password" name="pwd" /> <br/>

        <input type="submit" value="Login!" />
    </form>

    <a href="register.py">Register</a>
""")

if os.environ["REQUEST_METHOD"].upper() == "POST" and not success:
    print("Login Error!")

html_base.end()
