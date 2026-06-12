import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def main():
    client = AsyncIOMotorClient("mongodb+srv://tajparaprincy_db_user:Princy131810@princy123.dnasagc.mongodb.net/testDB?retryWrites=true&w=majority")

    db = client["testDB"]
    collection = db["users"]

    async for user in collection.find():
        print(user)

    print("Connected to MongoDB Atlas using Motor 🚀")

asyncio.run(main())