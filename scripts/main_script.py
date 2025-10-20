##########################
#Script principal pour la  Migration ou le CRUD: Automatisé ou interactif 
###########################

import pandas as pd
from pymongo import MongoClient # Connexion et gestion MongoDB
import argparse                 # Gestion des arguments
import getpass                  # Saisie sécurisée de mot de passe


# Import des fonctions définies
from def_choisir_ou_creer_base import choisir_ou_creer_base
from def_choisir_ou_creer_collection import choisir_ou_creer_collection
from def_choisir_ou_creer_cles import choisir_ou_creer_cles
from def_inserer_document_manuellement import inserer_document_manuellement
from def_nettoyer_et_migrer_csv import nettoyer_et_migrer_csv


# Création et definition des arguments possibles pour l'automatisation
parser = argparse.ArgumentParser(description="Gestion MongoDB")
parser.add_argument("--csv", help="Chemin fichier CSV pour migration automatisée")
parser.add_argument("--db", help="Nom de la base")
parser.add_argument("--collection", help="Nom de la collection")
parser.add_argument("--user", help="Nom de l'utilisateur")
parser.add_argument("--password", help="Mot de passe de l'utilisateur")
parser.add_argument("--pas_vider_col", action="store_false", help="Pour ne pas vider la collection avant ajout") # 
args = parser.parse_args()
    
# Si l’utilisateur n’a pas précisé son identifiant ou son mot de passe dans les arguments, il doit les entrer manuellement
if not args.user:
        args.user=input ("Entrer votre identifiant :").strip()
if not args.password:
       args.password=getpass.getpass("Entrer votre mots de passe :")

# Test de connexion à MongoDB avec les identifiants
try:
        client = MongoClient(f"mongodb://{args.user}:{args.password}@mongo:27017/") 
        client.admin.command("ping") 
except Exception :
        client=None


##############
#Mode automatisé avec arguments
#################

# On vérifie qu'il y a bien un fichier CSV, une base et une collection pour traiter la migration.

if args.csv and args.db and args.collection and ( client is not None):
        db = client[args.db]                                                    #Selectione ou crée la base de donnée spécifiée par l'argument --db 
        collection = db[args.collection]                                        #Selectione ou crée la collection spécifiée par l'argument --collection
        nettoyer_et_migrer_csv(db, collection, args.csv, args.pas_vider_col)    #Lance la fonction de migration du  fichier csv avec un nettoyage 
elif client is None:
        print("Erreur d'identifiant ou de mot de passe")

else:
    
#########
# Mode interactif: s'active s'il manque au moins un argument essentiel pour la migration (csv, db , collection) 
#########

    print("\n\n************************************\n* Gestion MongoDB : MODE INTERACTIF pour CRUD*\n************************************")
    db = choisir_ou_creer_base(client)                  #Permet de choisir ou de créer une base de données cible pour la migration
    if db is not None:
      collection = choisir_ou_creer_collection(db)      #Permet de choisir ou de créer une collection dans la base cible
      if collection is not None:
          while True:
            print("""
        1. Gérer les clés  # CRUD des clés 
        2. Insérer un document manuellement
        3. Migrer depuis CSV
        4. Quitter
        """)
            choix = input("Votre choix : ").strip()
            if choix=="1":
              choisir_ou_creer_cles(db, collection)  #Choisir ou créer des clés dans la collection "cles" afin de faciliter l’ajout de documents dans la collection cible.
            elif choix=="2":
              inserer_document_manuellement(db, collection) #Permet d’insérer manuellement des documents dans la collection cible choisie
            elif choix=="3":
             csv_file = input("Chemin du CSV : ").strip()
             nettoyer_et_migrer_csv(db, collection, csv_file,args.pas_vider_col)  #Lance la fonction de migration du fichier CSV avec un nettoyage préalable. La collection est vidée par default 
            elif choix=="4":
               break
            else:
             print("Choix invalide.")



