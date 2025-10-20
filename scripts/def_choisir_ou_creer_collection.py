##########################
#Fonction pour creer ou choisir une collection via le mode interactif  
###########################
from pymongo import MongoClient


def choisir_ou_creer_collection(db):
    while True:
        collections = db.list_collection_names()
        collections= [b for b in collections if b not in ("cles")]
              
                     

        if collections:
            print("\n Collections disponibles ")
            for i, nom in enumerate(collections):
                print(f"[{i}] {nom}")
            choix = input("\nVoulez-vous sélectionner une collection existante  (oui ou non)? ").strip().lower()
            if choix == "oui":
                try:    
                    index = int(input("Entrer le numéro pour sélectionner la collection : ").strip())
                    if index < len(collections):
                        nom = collections[index]
                        print(f"Collection '{nom}' sélectionnée.")
                        return db[nom]
                except:
                   print("Réponse invalide.")
                                 
            elif choix == "non":
                choix2 = input("\nVoulez-vous creer une collection (oui ou non)? ").strip().lower()               
                if choix2=='oui':
                    nom = input("Entrer le nom de la nouvelle collection : ").strip()
                    if nom:
                        print(f"Collection '{nom}' créée.")
                        return db[nom]
                else: 
                  return None
            else:
                print("Réponse invalide.")
        
        else:
               choix2 = input("\nAucune collection n'est disponible. Voulez-vous creer une collection (oui ou non)? ").strip().lower()               
               if choix2=='oui':
                    nom = input("Entrer le nom de la nouvelle collection : ").strip()
                    if nom:
                        print(f"Collection '{nom}' créée.")
                        return db[nom]
               else: 
                   return None

