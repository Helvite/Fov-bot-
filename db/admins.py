import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError

DATABASE_NAME = "fov"
DATABASE_URL = "mongodb://localhost:27017/"  


async def create_database_and_collection():
    try:
        client = AsyncIOMotorClient(DATABASE_URL)
        db = client[DATABASE_NAME]
        collection = db["admins"]
        await collection.create_index([("tg_id", 1)], unique=True)
        print(f"База данных '{DATABASE_NAME}' и коллекция 'users' созданы (или уже существуют).")
        return collection
    except Exception as e:
        print(f"Ошибка создания базы данных или коллекции: {e}")
        return None


async def add_admin():
    try:
        client = AsyncIOMotorClient(DATABASE_URL)
        db = client[DATABASE_NAME]
        collection = db["admins"]
        
        await collection.insert_many([
                {"tg_id": 1905121720}])

    except DuplicateKeyError:
            print(f"Пользователь уже существует.")

