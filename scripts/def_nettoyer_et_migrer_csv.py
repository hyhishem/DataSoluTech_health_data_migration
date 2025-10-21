##########################
#Fonction pour nettoyer le dataset et faire la migration dans Mongodb
###########################


import pandas as pd
from pymongo import MongoClient
import os         # interaction avec le system et les variables d’environnement


def nettoyer_et_migrer_csv(db, collection, csv_file, pas_vider_col):
    if not os.path.exists(csv_file): #verifie le path du fichier avant lecture
        print(f"Fichier introuvable : {csv_file}")
        return
    df = pd.read_csv(csv_file)


###############
# Nettoyer et uniformisation du dataset
###############

    df["Name"] = df["Name"].astype(str).str.strip().str.title()                 # Mise en forme des noms 1ère lettre en majuscule
    df["Billing Amount"] = pd.to_numeric(df["Billing Amount"]).round(2) 
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], format="%Y-%m-%d")
    df["Discharge Date" ] = pd.to_datetime(df["Discharge Date" ], format="%Y-%m-%d")
   
        
######   
# Supprimer doublons
######
    df = df.drop_duplicates()
    df = df[~df[["Name","Date of Admission","Room Number"]].duplicated()] # unicité Nom date d'admission et numero de chambre avant création de l'index
    
    if pas_vider_col: # par default vrais sauf si on ajout l'argument pas_vider_col
        try :
            collection.delete_many({})
            print(f"Tous les documents de la collection {collection.name} ont été supprimé.")
        except Exception as e:
           if  "not authorized" in  e.details.get("errmsg", str(e)).lower():      
                print("Vous n'avez pas les droits pour supprimer des documents.")
           else:
             print("Erreur mongo :" , e.details.get("errmsg", str(e)) )
    
    documents = df.to_dict("records")  # conversion de df en dictionnaire 
    
    if documents:
        try:
            collection.insert_many(documents, ordered=False) 
            print(f"{len(documents)} documents insérés dans {collection.name}.")
        except Exception as e:
           if  "not authorized" in  e.details.get("errmsg", str(e)).lower():      
                print("Vous n'avez pas les droits pour ajouter des documents.")
           else:
                print("Erreur mongo :" , e.details.get("errmsg", str(e)) )

    else:
        print("Aucun document valide.")
    
    collection.create_index([("Name", 1), ("Age", 1), ("Date of Admission", 1), ("Room Number", 1)],unique=True, name="index_name_date_room") # Creation de l'index
    return

######### 
# Test de l'unicité de l'index
########  

    try:    
       doc = collection.find_one({}, {"_id": 0, "Name": 1, "Date of Admission": 1, "Room Number": 1})
       print(f'{doc}')
       collection.insert_one(doc)       
    except Exception as e:
        if "duplicate key" in str(e).lower():
            print("L'unicité de l'index  défini empêche l'ajout de certains documents")
       
       
        
