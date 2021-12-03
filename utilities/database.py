# Connect to arangoDB database
# using login and password
login = "root"
password = "testtest"
# open arango db
url = "http://localhost:8529"
from pyArango.connection import *
print("Connecting to arangoDB")
conn = Connection(arangoURL=url, username=login, password=password)
print("Connected to arangoDB")
# create database and collections
try:
    db = conn.createDatabase(name="Preprocessing")
    print("Database created")
except Exception as e:
    print("Database already exists")
    db = conn["Preprocessing"]
try:
    collection = db.createCollection(name="CSV_data")
    print("Collection created")
except Exception as e:
    print("Collection already exists")
    collection = db["CSV_data"]

def add_documents( notes, checkboxes, headers):
    doc = collection.createDocument()
    doc["notes"] = notes
    doc["checkboxes"] = checkboxes
    doc["headers"] = headers
    doc.save()
    return doc._key
def lookup_documents(collection, key):
    return collection.fetchDocument(key)

notes = ["This is a test note"]
checkboxes = ["This is a test checkbox"]
headers = ["This is a test header"]
# key = "test"

# key = add_documents(collection, notes, checkboxes, headers)

# print(lookup_documents(collection, key))
# print(key)

    
    


