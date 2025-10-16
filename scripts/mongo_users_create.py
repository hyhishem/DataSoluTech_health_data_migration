from pymongo import MongoClient
import os

client =  MongoClient(f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@mongo:27017/")
db = client["admin"]


try:
    db.command("createUser", os.getenv("MONGO_RW_USER"),
            pwd=os.getenv("MONGO_RW_PASS"),
            roles=[{"role":"readWriteAnyDatabase","db":"admin"}])
except Exception as e:
    print('Erreur :', e.details.get("errmsg", str(e)) )



try:
    db.command("createUser", os.getenv("MNGO_READ_USER"), 
            pwd=os.getenv("MONGO_READ_PASS"),
            roles=[{"role":"readAnyDatabase","db":"admin"}])
except Exception as e:
    print('Erreur :', e.details.get("errmsg", str(e)) )




