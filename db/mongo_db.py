import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError
import datetime

DATABASE_NAME = "fov"
DATABASE_URL = "mongodb://localhost:27017/"  


async def create_database_and_collection():
    try:
        client = AsyncIOMotorClient(DATABASE_URL)
        db = client[DATABASE_NAME]
        collection = db["users"]
        await collection.create_index([("tg_id", 1)], unique=True)
        print(f"База данных '{DATABASE_NAME}' и коллекция 'users' созданы (или уже существуют).")
        return collection
    except Exception as e:
        print(f"Ошибка создания базы данных или коллекции: {e}")
        return None




class MongoDB:
    def __init__(self):
        client = AsyncIOMotorClient(DATABASE_URL)
        db = client[DATABASE_NAME]
        self.collection = db["users"]



    async def insert_or_update_user(self, tg_id, user_data):
        try:
            await self.collection.update_one(
                {"tg_id": tg_id}, {"$set": {"tg_id": tg_id}, "$setOnInsert": {"language": None, "registration_time": datetime.datetime.now(datetime.timezone.utc)}}, upsert=True)
        
        except DuplicateKeyError:
            print(f"Пользователь с tg_id {tg_id} уже существует.")
        except Exception as e:
            print(f"Ошибка вставки/обновления пользователя: {e}")


    async def set_user(self,tg_id):
        try:
            user = await self.collection.find_one({"tg_id": tg_id})

            if user is None:
                new_user = {
                    "tg_id": tg_id,
                    "registration_time": datetime.datetime.now(datetime.timezone.utc)
                }
                await self.collection.insert_one(new_user)
        except Exception as e:
            print(f"Ошибка обработки: {e}")

        

    async def set_user_language(self, tg_id, language):
        try:
            await self.collection.update_one({"tg_id": tg_id}, {"$set": {"language": language}})
        except Exception as e:
            print(f"Ошибка обновления языка: {e}")
        

    async def get_user_language(self, tg_id):
        try:
            user = await self.collection.find_one({"tg_id": tg_id})
            return user["language"] if user else None
        except Exception as e:
            print(f"Ошибка получения языка пользователя: {e}")
            return None


    async def get_user_balance(self, tg_id):
        try:
            user = await self.collection.find_one({"tg_id": tg_id})
            return user["balance"] if user else None
        except Exception as e:
            print(f"Ошибка получения: {e}")
            return None

    async def set_user_balance(self, tg_id, balance):
        try:
            user = await self.collection.find_one({"tg_id": tg_id})
            if user:
                current_user_balance = user['balance']
            current_balance = balance + current_user_balance
            await self.collection.update_one({"tg_id": tg_id}, {"$set": {"balance": current_balance}})
        except Exception as e:
            print(f"Ошибка обновления: {e}")

    
    async def user_buy_chat(self, tg_id, buy):
        try:
            await self.collection.update_one({"tg_id": tg_id}, {"$set": {"private_chat": buy}})
        except Exception as e:
            print(f"Ошибка: {e}")


async def main():
    await create_database_and_collection()
    

if __name__ == "__main__":
    asyncio.run(main())
