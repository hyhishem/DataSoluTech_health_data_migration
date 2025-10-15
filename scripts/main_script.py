#!/usr/bin/env python3

import pandas as pd
from pymongo import MongoClient
from datetime import datetime
import argparse
import os
import getpass

from def_choisir_ou_creer_base import choisir_ou_creer_base
from def_choisir_ou_creer_collection import choisir_ou_creer_collection
from def_choisir_ou_creer_cles import choisir_ou_creer_cles
from def_inserer_document_manuellement import inserer_document_manuellement
from def_nettoyer_et_migrer_csv import nettoyer_et_migrer_csv

def main():
    parser = argparse.ArgumentParser(description="Gestion MongoDB interactive et automatisée")
    parser.add_argument("--csv", help="Chemin fichier CSV pour migration automatisée")
    parser.add_argument("--db", help="Nom de la base")
    parser.add_argument("--collection", help="Nom de la collection")
    parser.add_argument("--user", help="Nom de l'utilisateur")
    parser.add_argument("--password", help="Mot de passe de l'utilisateur")
    parser.add_argument("--vider_col", action="store_false", help="Vider la collection avant ajout")
    args = parser.parse_args()
    if not args.user:
        args.user=input ("Entrer votre identifiant :").strip()
    if not args.password:
       args.password=getpass.getpass("Entrer votre mots de passe :")
    
       
    client=None
    try:
        client = MongoClient(f"mongodb://{args.user}:{args.password}@mongo:27017/") 
        client.admin.command("ping") 
    except Exception :
        client=None

    if args.csv and args.db and args.collection and ( client is not None):
        ##########
        # Mode automatisé
        #########
        db = client[args.db]
        collection = db[args.collection]
        nettoyer_et_migrer_csv(db, collection, args.csv, args.vider_col)
            
    elif client is None:
        print("Erreur d'identifiant ou de mot de passe")
    else:
        #########
        # Mode interactif
        #########
        print("\n\n************************************\n* Gestion MongoDB : MODE INTERACTIF *\n************************************")
        db = choisir_ou_creer_base(client)
        if db is not None:
            collection = choisir_ou_creer_collection(db)
            if collection is not None:
                while True:
                    print("""
    1. Gérer les clés 
    2. Insérer un document manuellement
    3. Migrer depuis CSV
    4. Quitter
    """)
                    choix = input("Votre choix : ").strip()
                    if choix=="1":
                        choisir_ou_creer_cles(db)
                    elif choix=="2":
                        inserer_document_manuellement(db, collection)
                    elif choix=="3":
                        csv_file = input("Chemin du CSV : ").strip()
                        nettoyer_et_migrer_csv(db, collection, csv_file)
                    elif choix=="4":
                        break
                    else:
                        print("Choix invalide.")


if __name__ == "__main__":
    main()

