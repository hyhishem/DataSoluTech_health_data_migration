#!/usr/bin/env python3

import pandas as pd
from pymongo import MongoClient


########################
#Demande du fichier
########################

dataset = input("Entrez le nom du fichier CSV: ").strip()

df = pd.read_csv(dataset)
print("\n \n Aperçu des premières lignes")
print(df.head())


print("\n \n Aperçu du types des colonnes")
print(df.dtypes)



################################################
#nettoyage et modification du type des colonnes  (Version manuelle)
################################################

df['Name']=df['Name'].str.title()  # Majuscule uniquement en debut pour uniformiser 

df['Billing Amount']=df['Billing Amount'].round(2) # Prendre uniquement deux decimales

df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], format='%Y-%m-%d') # Format date 
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'], format='%Y-%m-%d') # Format date 

#############################
#Suppression des doublons 
##############################
lignes_avant = len(df) #  Nombre de lignes avant de supprimer les doublons
df = df.drop_duplicates() # Suppression des doublons
df=df[~df[['Name' ,'Date of Admission', 'Discharge Date', 'Room Number']].duplicated()] # Suppression des doublons partiel non probable 
lignes_apres = len(df)  #  Nombre de lignes après avoir supprimer les doublons

print(f" \n \n {lignes_avant - lignes_apres} doublons ont été supprimés")


######################
# Aperçu final 
######################

print("\n \nAperçu final \n \n:") #Visuel après nettoyage
print("\n \n Aperçu des premières lignes")  
print(df.head())


print("\n \n Aperçu du types des colonnes")
print(df.dtypes)


######################
# Migration df ---> Collection mongo
######################

######################
# Connexion
######################

client = MongoClient("mongodb://admin:admin123@mongo:27017/")

######################
# CRUD
######################

#connexion ou création base/collection

db = client["health_data"]        # Nom de la base 
collection = db["patients"]       # Nom de la collection


reponse = input("Voulez-vous supprimer TOUS les documents de la collection ? (oui/non): ").strip().lower()

if reponse == "oui":
    collection.delete_many({})
    print("Tous les documents ont été supprimés.")
else:
    print("Suppression annulée.")


#inserer un document

input("Appuyez sur Entrée pour inserer les documents:")

doc = {
    "Name": "Bobby Jackson",
    "Date of Admission": "2024-01-31",
    "Billing Amount": 18856.28,
    "Room Number": 328,
    "Discharge Date": "2024-02-02"
}
collection.insert_one(doc)


doc = {
    "Name": "Leslie Terry",
    "Date of Admission": "2019-08-20",
    "Billing Amount": 33643.33,
    "Room Number": 265,
    "Discharge Date": "2019-08-26"
}
collection.insert_one(doc)

print("Verifier l'insertion sur mongo-express")


#Lecture 

input("Appuyez sur Entrée pour afficher les patients:")
for doc in collection.find({}):
    print(doc)

#Mise à jour d'un document

input("Appuyez sur Entrée pour ajouter l'age:")
collection.update_one(
    {"Name": "Bobby Jackson"},
    {"$set": {"Age": 30}},
    upsert=True  # crée le document s’il n’existe pas
)

collection.update_one(
    {"Name": "Leslie Terry"},
    {"$set": {"Age": 62}},
    upsert=True  # crée le document s’il n’existe pas
)

print("Verifier la mise à jour sur mongo-express")

#Suppression d'un document
input("Appuyez sur Entrée pour supprimer tous les documents de la collection:")
collection.delete_many({})

print("Verifier la suppression sur mongo-express")


################################################
# Insérer toutes les données du dataframe df
################################################

input("Appuyez sur Entrée pour réaliser  la migration du dataframes nettoyé:")

collection.insert_many(df.to_dict("records")) 

print("Verifier sur mongo-express")

