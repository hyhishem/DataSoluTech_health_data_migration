##########################
#Ce script crée différents rôles utilisateurs
###########################

from pymongo import MongoClient
import os #acceder au variable d'environement

client =  MongoClient(f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@mongo:27017/") #connexion root admin pour la gestion
db = client["admin"] #Selectionner la base de donnée admin


try:
    db.command("createUser", os.getenv("MONGO_RW_USER"),
            pwd=os.getenv("MONGO_RW_PASS"),
            roles=[{"role":"readWriteAnyDatabase","db":"admin"}]) # création d'un nouvelle utilisateur read + write
except Exception as e:
    print('Erreur :', e.details.get("errmsg", str(e)) )



try:
    db.command("createUser", os.getenv("MNGO_READ_USER"), 
            pwd=os.getenv("MONGO_READ_PASS"),
            roles=[{"role":"readAnyDatabase","db":"admin"}])  # création d'un nouvelle utilisateur read seulement
except Exception as e:
    print('Erreur :', e.details.get("errmsg", str(e)) )




