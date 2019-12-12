#!C:\Users\Mateo\AppData\Local\Programs\Python\Python38\python.exe

import html_base
import courseList
import session
import os
import cgi

courses = courseList.giveYear2()
parameters = cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.addSession(parameters)

data = session.getData()

html_base.start()

print('<form action="" method="POST">')
print('<table>')

for c in courses['subject']:
    print('<tr>')
    print('<td>' + c + '</td>')
    print('<td><input type="radio" name="status' + c + '" value="N" ' + ('checked' if data.get('status' + c) is 'N' else '') + ' >Ne upisuje</td>')
    print('<td><input type="radio" name="status' + c + '" value="U" ' + ('checked' if data.get('status' + c) is 'U' else '') + '>Upisuje</td>')
    print('<td><input type="radio" name="status' + c + '" value="P" ' + ('checked' if data.get('status' + c) is 'P' else '') + '>Polozen</td>')
    print('</tr>')

print('</table>')
print('<input type="submit" value="Potvrdi">')
print('</form>')

html_base.end()
