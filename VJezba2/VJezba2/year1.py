#!C:\Users\Mateo\AppData\Local\Programs\Python\Python38\python.exe

import html_base
import courseList
import session
import os
import cgi

courses = courseList.giveYear1()
parameters = cgi.FieldStorage()
#data =
#session.getData()

html_base.start()
if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    pass
    #session.addSession(parameters)
i = 0

print('<form action="" method="POST">')
print('<table>')

for c in courses['subject']:
    print('<tr>')
    print('<td>' + c + '</td>')
    print('<td><input type="radio" name="status' + str(i) + '" value="N" ' + '' + ' >Ne upisuje</td>') #umjesto zadnjed '' ide checked i to - ('checked' if data['status' + str(i)] else '')
    print('<td><input type="radio" name="status' + str(i) + '" value="U" ' + '' + '>Upisuje</td>')
    print('<td><input type="radio" name="status' + str(i) + '" value="P" ' + '' + '>Polozen</td>')
    print('</tr>')
    i += 1

print('</table>')
print('<input type="submit" value="Potvrdi">')
print('</form>')

#print(parameters)

html_base.end()
