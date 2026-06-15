from pymongo import MongoClient

MONGO_URL = "mongodb+srv://tajparaprincy_db_user:Prinsi%401310@week-7-day-5.4ufn9sf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URL)

db = client["analytics_db"]

activity_collection = db["activity_logs"]