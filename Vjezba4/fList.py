#!C:\Users\Mateo\AppData\Local\Programs\Python\Python38\python.exe

import html_base
import courseList
import session
import os
import cgi

cList =  [courseList.giveYear1(), courseList.giveYear2(), courseList.giveYear3()]
sum = 0
data = session.getData()

html_base.start()
html_base.tableHead()
for courses in cList:
    for i in range(len(courses.get('subject'))):
        status = data.get('status' + courses.get('subject')[i])
        if status is "U":
            statusMessage = "Upisano"
            sum += int(courses.get('ECTS')[i])
        elif status is "P":
            statusMessage = "Polozeno"
        else:
            statusMessage = "Nije upisano"

        print('<tr>')
        print('<td>' + courses.get('subject')[i] + '</td>')
        print('<td>' + statusMessage + '</td>')
        print('<td>' + courses.get('ECTS')[i] + '</td>')
        print('</tr>')
html_base.tableFoot(sum)
html_base.end()
