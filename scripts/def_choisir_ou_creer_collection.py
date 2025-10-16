from pymongo import MongoClient


def choisir_ou_creer_collection(db):
    while True:
        collections = db.list_collection_names()
        collections_utile= [b for b in collections if b not in ("cles")]
        collections=collections_utile
        print("\n Collections disponibles ")
        for i, nom in enumerate(collections):
            print(f"[{i}] {nom}")
        choix = input("\nVoulez-vous sélectionner une collection existante  (oui ou non)? ").strip().lower()
        if choix == "oui":
            if not collections:
                print("Aucune collection existante.")
                continue
            index = input("Entrer le numéro pour sélectionner la collection : ").strip()
            if index.isdigit() and int(index) < len(collections):
                nom = collections[int(index)]
                print(f"Collection '{nom}' sélectionnée.")
                return db[nom]
            else:
                print("Réponse invalide.")
                continue
            
        elif choix == "non":
            nom = input("Nom de la nouvelle collection : ").strip()
            if nom:
                print(f"Collection '{nom}' créée.")
                return db[nom]
        elif choix == "exit":
            return None
        else:
            print("Réponse invalide.")



