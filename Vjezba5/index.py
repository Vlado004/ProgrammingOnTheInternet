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

currCollectionID = session.getCurrCollection()
collections = database.getCollectionIDs()
if currCollectionID:
    for coll in collections:
        if currCollectionID == str(coll[0]):
            currCollection = coll[1]
            break
else:
    currCollectionID = collections[0][0]
    currCollection = collections[0][1]

if os.environ["REQUEST_METHOD"].upper() == "POST":
    parameters = cgi.FieldStorage()
    collectionSelect = parameters.getvalue("collectionSelect")
    newCollection = parameters.getvalue("newCollection")

    if collectionSelect:
        session.setCollection(collectionSelect)
        print("Location: index.py")

    if newCollection is not None:
        database.createCollection(newCollection)

    if "upload" in parameters:
        file = parameters["image"]
        if file.filename is not None:
            fn = ('image/')
            fn += os.path.basename(file.filename)
            database.uploadImage(file, currCollectionID)
            open(fn, 'wb').write(file.file.read(2500000))

html_base.start()

print('<form method="POST">')
print("Selected collection: <i>" + currCollection + "</i><br/>")
print('<select name="collectionSelect">')
for coll in collections:
    print('<option value="' + str(coll[0]) + '" ' + ("selected" if str(coll[0]) == str(currCollectionID) else "") + ' >' + coll[1] +'</option>')
print("""    </select>
    <input type="submit" value="Select"><br/>

    New collection:<br/>
        <input type="text" name="newCollection">
        <input type="submit" value="Submit">
    </form>
    """)

print("""<form enctype="multipart/form-data" method="POST">
  <input type="file" name="image" accept="image/*">
  <input type="submit" name="upload" value="Upload" />""")
print('<input type="hidden" name="collection_id" value="' + str(currCollectionID) + '" />')
print("</form>")


pictures = database.getImagesViaCollectionID(currCollectionID)
for pic in pictures:
    print('<a href="detail.py?image_id='+ str(pic[0]) + '"><img src="image/' + pic[1] + '" alt="' + str(pic[0]) + '" /></a>')#'<a href="imageDetail.py?imageID' + pic[1]'">' - to ce stvorit get request pa cu moc pristupat slici preko FieldStorage s imageID
#SLike

print('<br/><a href="logout.py">Logout</a></br>')
print('<a href="change_password.py">Change password</a>')
if user_role == "admin":
    print('<br/><a href="admin.py">Check counters (ADMIN ONLY)</a>')

html_base.end()
