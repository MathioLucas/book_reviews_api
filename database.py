import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.book_review

book_collection = database.get_collection("books")

review_collection = database.get_collectoin("book_review")

