def start():
    print ("Content-type:text/html\r\n\r\n")

    print("""
    <!DOCTYPE HTML>
    <html>
        <head>
            <meta charset="UTF-8">
        </head>

        <body>
            <table>
                <tr>
                    <td><a href="year1.py">1. Godina</td>
                    <td><a href="year2.py">2. Godina</td>
                    <td><a href="year3.py">3. Godina</td>
                    <td><a href="fList.py">Upisni list</td>
                </tr>
            </table>""")

def end():
    print("""        </body>
    </html>
    """)

def tableHead():
    print("""<table>
    <tr>
    <th>Predmet</th>
    <th>Status</th>
    <th>ECTS</th>
    </tr>""")

def tableFoot(sum):
    print("""<tr>
    <td>.</td>
    <td>Ukupno:</td>
    <td>""" + str(sum) + """</td>
    </tr>
    </table>""")
