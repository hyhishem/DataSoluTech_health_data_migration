##########################
#Fonction pour creer ou choisir une base via le mode interactif  
###########################

from pymongo import MongoClient

def choisir_ou_creer_base(client):
    while True:
        bases = client.list_database_names()
        print("\nBases disponibles")
        bases_utile= [b for b in bases if b not in ("admin", "config", "local")]
        bases=bases_utile
        for n, nom in enumerate(bases):
            print(f"[{n}] {nom}")
        if not bases:
            print("Aucune base existante.")
            choix = input("\nVoulez-vous creer une nouvelle base (oui ou non)? ").strip().lower()
            if choix=='oui':
                nom = input("Entrer le nom de la nouvelle base : ").strip()
                if nom:
                   print(f"Base '{nom}' créée.")
                   return client[nom]
            else:
                return None
        elif bases:
            choix = input("\nVoulez-vous sélectionner une base existante(oui ou non)? ").strip().lower()
            if choix == "oui":
                try:
                    index = int(input("Entrer le numéro pour sélectionner la base : ").strip())
                    if index < len(bases):
                        nom = bases[index]
                        print(f"Base '{nom}' sélectionnée.")
                        return client[nom]
                except:
                   print("Réponse invalide.")
            elif choix == "non":
                choix = input("\nVoulez-vous creer une nouvelle base (oui ou non)? ").strip().lower()
                if choix=='oui':
                    nom = input("Entrer le nom de la nouvelle base : ").strip()
                    if nom:
                        print(f"Base '{nom}' créée.")
                        return client[nom]
                else:
                    return None
            elif choix == "exit":
                return None
            else:
                print("Réponse invalide.")
