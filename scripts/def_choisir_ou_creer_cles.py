from pymongo import MongoClient


def choisir_ou_creer_cles(db):
    collection_cles = db["cles"]
    while True:
        cles = list(collection_cles.find({}, {"_id":0}))
        print("\nClés existantes")
        for i, c in enumerate(cles):
            print(f"[{i}] {c['nom_cle']} (type: {c['type_cle']})")
        choix = input("\nVoulez-vous ajouter une clé (oui ou non)? ").strip().lower()
        if choix == "oui":
            nom_cle = input("Nom de la nouvelle clé : ").strip()
            types = ["str", "int", "float", "date"]
            for idx, t in enumerate(types):
                print(f"[{idx}] {t}")
            type_index = input("Type de la clé (0-3) : ").strip()
            if type_index.isdigit() and int(type_index) < len(types):
                collection_cles.insert_one({"nom_cle": nom_cle, "type_cle": types[int(type_index)]})
                print(f"Clé '{nom_cle}' ajoutée.")
        elif choix == "non":
            return list(collection_cles.find({}, {"_id":0}))
        else:
            print("Réponse invalide.")



