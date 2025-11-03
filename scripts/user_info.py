from pymongo import MongoClient # Connexion et gestion MongoDB


try:
        client = MongoClient(f"mongodb://admin:admin123@mongo:27017/") 
        client.admin.command("ping") 
except Exception :
        client=None


db=client.admin
docs=db.command("usersInfo")["users"]

for i in range(len(docs)):
    print(f"\n User:{docs[i]['user']} ; Roles:{docs[i]['roles']}, Mechanisms:{docs[i]['mechanisms']} \n")
