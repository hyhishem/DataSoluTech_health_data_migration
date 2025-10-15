#!/usr/bin/env python3

import pandas as pd
from pymongo import MongoClient
from datetime import datetime
import os


def nettoyer_et_migrer_csv(db, collection, csv_file, vider_col):
    if not os.path.exists(csv_file):
        print(f"Fichier introuvable : {csv_file}")
        return
    df = pd.read_csv(csv_file)


#########
# Nettoyer 
#########
    df["Name"] = df["Name"].astype(str).str.title()
    df["Billing Amount"] = pd.to_numeric(df["Billing Amount"], errors="coerce").round(2)
    for col in ["Date of Admission","Discharge Date"]:
        df[col] = pd.to_datetime(df[col], errors="coerce", format="%Y-%m-%d")
        
######   
# Supprimer doublons
######
    df = df.drop_duplicates()
    df = df[~df[["Name","Date of Admission","Room Number"]].duplicated()]
    
    if vider_col:
        try :
            collection.delete_many({})
            print("Tous les documents de la collection ont été supprimer")
        except Exception as e:
           if  "not authorized" in  e.details.get("errmsg", str(e)).lower():      
                print("Vous n'avez pas les droits pour supprimer des documents.")
           else:
             print("Erreur mongo :" , e.details.get("errmsg", str(e)) )
    documents = df.to_dict("records")
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
    try:    
        collection.create_index([("Name", 1), ("Date of Admission", 1), ("Room Number", 1)],unique=True, name="index_name_date_room")
    except Exception:
        return None



