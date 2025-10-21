##########################
#Fonction gestion des clés: importer, creer, modifier ou supprimer des clés pour le mode interactif.  Les clé et types sont stockés dans la collection "cles"
###########################
from pymongo import MongoClient


def choisir_ou_creer_cles(db, collection):
    collection_cles = db["cles"] # Créer ou choisir une collection composée des clés et du type afin de réduire l'erreur et de faciliter l'ajout manuel.   
    
    docs_1 = collection.find({}, {"_id": 0}).limit(1)    # clés présentes dans la collection cible


    try:
        collection_cles.create_index([("nom_cle")], unique=True, name="index_nom_cle") # index pour imposer l'unicité des clés
    except:
        None


############
# Importer les clés  et types de la collection cible vers la collection cles
#########

    if docs_1:
        choix=input('Voulez vous importer les clés disponible? (oui ou non):').strip()
        if choix=='oui':
            for doc in docs_1:
              for nom_cle, valeur in doc.items():
                try:
                    collection_cles.insert_one({'nom_cle':nom_cle, 'type_cle':type(valeur).__name__ })  
                except Exception as e: 
                    if "duplicate key" in e.details.get("errmsg", str(e)).lower(): # Se déclenche si l'unicité des clés n'est pas respectée. 
                        print(f'La clé {nom_cle} est déja présente')
                    else:
                        print("Erreur mongo :" , e.details.get("errmsg", str(e)) )
                    

#########
# Inserer une nouvelle clé   
############     
     
    while True:
        choix = input("\nVoulez-vous ajouter une clé manuellement (oui ou non)? ").strip().lower()
        if choix == "oui":
            nom_cle = input("Nom de la nouvelle clé : ").strip()
            types = ["str", "int", "float", "date"]
            for n, t in enumerate(types):
                print(f"[{n}] {t}")
            type_index = int(input("Type de la clé (0-3) : ").strip())
            try:
                if type_index < len(types):
                    try:
                        collection_cles.insert_one({"nom_cle": nom_cle, "type_cle": types[type_index]})
                        print(f"\nLa clé '{nom_cle}' est ajouté\n.")
                    except:
                        print(f'\nLa clé {nom_cle} est déja présente\n')
            except:
                print("Réponse invalide.")
        elif choix == "non":
            break
        else:
            print("Réponse invalide.")
            





    while True:
    
#########
# Afficher les documents de la collection "cles"    
############

        cles = list(collection_cles.find({}, {"_id":0}))
        print("\nListe des clés existantes\n:") 
        for n, c in enumerate(cles):
            print(f"[{n}] {c['nom_cle']} (type: {c['type_cle']})")


#########
# Modifier le nom d'une clé   
#########               

        choix = input(f"\nSouhaitez-vous renommer une clé de la collection {collection_cles.name}?  (oui ou non) ").strip().lower()
        if choix == "oui":
            cle_index = int(input(f"\nIndiquer l'index relatif à la clé que vous souhaitez modifier :").strip())
            ancienne_cle=cles[cle_index]['nom_cle']              
            nouvelle_cle = input(f"\n Entrer la nouvelle valeur :").strip()
            try:    
               if 0<= cle_index <len(cles):
                  collection_cles.update_one({"nom_cle": ancienne_cle},{"$set": {"nom_cle": nouvelle_cle}})
            except:
               print("Réponse invalide.")
        elif choix == "non":
            None
        else:
            print("Réponse invalide.")

#########
# Modifier le type de la clé   
#########               

        choix = input(f"\nSouhaitez-vous modifier le type d'une clé de la collection {collection_cles.name}?  (oui ou non) ").strip().lower()
        if choix == "oui":
                cle_index = int(input(f"\nIndiquer l'index relatif à la clé que vous souhaitez modifier :").strip())
                nom_cle=cles[cle_index]['nom_cle']  
                ancien_type=cles[cle_index]['type_cle'] 
                
                print(f'ancien type {ancien_type}')
                
                types = ["str", "int", "float", "date"]
                for n, t in enumerate(types):
                        print(f"[{n}] {t}")
                type_index = int(input("Type de la clé (0-3) : ").strip())
                
                nouveau_type=types[type_index]
                try:    
                    if 0<= cle_index <len(cles):
                         collection_cles.update_one({"nom_cle": nom_cle},{"$set": {"type_cle": nouveau_type}})
                except:
                    print("Réponse invalide.")      
        elif choix == "non":
            None
        else:
            print("Réponse invalide.")
        
 
#########
# Suppression   
#########               

            
        choix = input(f"\nSouhaitez-vous supprimer tous les documents de la collection {collection_cles.name}?  (oui ou non) ").strip().lower()
        if choix == "oui":
            collection_cles.delete_many({})     
        elif choix == "non":
            None
        else:
            print("Réponse invalide.")


        choix = input(f"\nSouhaitez-vous supprimer un document de la collection {collection_cles.name}?  (oui ou non) ").strip().lower()
        if choix == "oui":
                try:
                    cle_index = int(input(f"\nIndiquer l'index relatif à la clé que vous souhaitez supprimer :").strip())
                    nom_cle=cles[cle_index]['nom_cle']  
                    if 0<= cle_index <len(cles):
                         collection_cles.delete_one({"nom_cle": nom_cle})
                except:
                    print("Réponse invalide.")      
        elif choix == "non":
            break
        else:
            print("Réponse invalide.")
            

