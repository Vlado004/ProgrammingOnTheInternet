#!C:\Program Files\Python 3.5\python.exe

import cgi
form_data = cgi.FieldStorage()

print('')
print (form_data.getvalue('ime'))
print (form_data.getvalue('smjer'))

