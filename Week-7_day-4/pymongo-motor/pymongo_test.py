from pymongo import MongoClient

# MongoDB Atlas connection string
client = MongoClient("mongodb+srv://tajparaprincy_db_user:Princy131810@princy123.dnasagc.mongodb.net/testDB?retryWrites=true&w=majority")

# Database
db = client["testDB"]

# Collection
collection = db["users"]

# Fetch and print data
for user in collection.find():
    print(user)

print("Connected to MongoDB Atlas Successfully 🚀")