##########################
#Script principal pour la  Migration ou le CRUD: Automatisé ou interactif 
###########################

import pandas as pd
from pymongo import MongoClient # Connexion et gestion MongoDB
import argparse                 # Gestion des arguments
import getpass                  # Saisie sécurisée de mot de passe


# Import des fonctions définies
from def_nettoyer_et_migrer_csv import nettoyer_et_migrer_csv
from def_crud_collection import crud_collection

# Création et definition des arguments possibles pour l'automatisation
parser = argparse.ArgumentParser(description="Gestion MongoDB")
parser.add_argument("--csv", help="Chemin fichier CSV pour migration automatisée")
parser.add_argument("--db", help="Nom de la base")
parser.add_argument("--collection", help="Nom de la collection")
parser.add_argument("--user", help="Nom de l'utilisateur")
parser.add_argument("--password", help="Mot de passe de l'utilisateur")
parser.add_argument("--pas_vider_col", action="store_false", help="Pour ne pas vider la collection avant ajout") 


parser.add_argument("--crud", help="Action CRUD: c-Create  r-Read  u-Update ou d-Delete")
parser.add_argument("--nom", default=None, help="Valeur pour la clé Name")
parser.add_argument("--age",type=int, default=None, help="Valeur pour la clé Age")
parser.add_argument("--new_nom", default=None, help="Nouvelle valeur pour la clé Name")
parser.add_argument("--new_age",type=int, default=None, help="Nouvelle valeur pour la clé Age")


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
#Mode automatisé avec arguments Migration de fichier csv ou CRUD
#################

# On vérifie qu'il y a bien un fichier CSV, une base et une collection pour traiter la migration.

if args.csv and args.db and args.collection and ( client is not None):
        db = client[args.db]                                                    #Selectione ou crée la base de donnée spécifiée par l'argument --db 
        collection = db[args.collection]                                        #Selectione ou crée la collection spécifiée par l'argument --collection
        nettoyer_et_migrer_csv(db, collection, args.csv, args.pas_vider_col)    #Lance la fonction de migration du  fichier csv avec un nettoyage 
elif client is None:
        print("Erreur d'identifiant ou de mot de passe")

elif args.crud and args.nom and args.db and args.collection and ( client is not None):
        db = client[args.db]                                                    #Selectione ou crée la base de donnée spécifiée par l'argument --db 
        collection = db[args.collection]                                        #Selectione ou crée la collection spécifiée par l'argument --collection
        crud_collection(db, collection,args.crud,args.nom, args.age, args.new_nom ,args.new_age)






