from pymongo import MongoClient

def choisir_ou_creer_base(client):
    while True:
        bases = client.list_database_names()
        print("\nBases disponibles")
        bases_utile= [b for b in bases if b not in ("admin", "config", "local")]
        bases=bases_utile
        for i, nom in enumerate(bases):
            print(f"[{i}] {nom}")
        choix = input("\nVoulez-vous sélectionner une base existante(oui ou non)? ").strip().lower()
        if choix == "oui":
            if not bases:
                print("Aucune base existante.")
                continue
            index = input("Entrer le numéro pour sélectionner la base : ").strip()
            if index.isdigit() and int(index) < len(bases):
                nom = bases[int(index)]
                print(f"Base '{nom}' sélectionnée.")
                return client[nom]
            else:
                print("Réponse invalide.")
        elif choix == "non":
            nom = input("Nom de la nouvelle base : ").strip()
            if nom:
                print(f"Base '{nom}' créée.")
                return client[nom]
        elif choix == "exit":
            return None
        else:
            print("Réponse invalide.")
