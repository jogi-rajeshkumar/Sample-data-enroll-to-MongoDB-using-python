import pymongo

# Connect to the local MongoDB instance
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a new database and collection
db = client["mydatabase"]
collection = db["mycollection"]

# Insert a document into the collection
document = {"name": "John", "age": 30}
insert_result = collection.insert_one(document)
print("Inserted document with ID:", insert_result.inserted_id)

# Retrieve all documents from the collection
documents = collection.find()
for doc in documents:
    print(doc)
