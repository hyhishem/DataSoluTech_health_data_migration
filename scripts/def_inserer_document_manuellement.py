##########################
#Fonction pour inserer manuellement un document
###########################
from pymongo import MongoClient
from datetime import datetime


def inserer_document_manuellement(db, collection, nom_doc=None, age_doc=None):


    cles = list(db["cles"].find({}, {"_id":0}))
    if not cles:
        print("Aucune clé disponible.")
        return
        

#########
# Afficher un documents de la collection    
############

    if nom_doc: 
        doc_nom= list(collection.find({'Name':nom_doc}, {"_id":0}))
        print(f"Résultats de votre recherche sur la clé 'Name': {nom_doc}:\n")
        print(f"{doc_nom}:\n")
    if age_doc:
        doc_age= list(collection.find({'Age':age_doc}, {"_id":0}))
        print(f"Résultats de votre recherche sur la clé 'Age': {age_doc}:\n")
        print(f"{doc_age}:\n")
    

    while True:
        choix = input("\nVoulez-vous insérer un document (oui ou non)?: ").strip().lower()
        if choix != "oui":
            break
        
        document = {}
        for cle in cles:
            valeur = input(f"Inserer une valeur pour '{cle['nom_cle']}' ({cle['type_cle']}).\nLaisser vide pour ignorer la clé : ").strip()
            if valeur == "":
                continue
            try:
                if cle["type_cle"]=="str":
                    valeur = str(valeur).title()
                elif cle["type_cle"]=="int":
                    valeur = int(valeur)
                elif cle["type_cle"]=="float":
                    valeur = float(valeur)
                elif cle["type_cle"]=="date" or cle["type_cle"]=="datetime":
                    valeur = datetime.strptime(valeur, "%Y-%m-%d")
            except ValueError:
                print(f"\n Valeur invalide pour '{cle['nom_cle']}', ignorée \n.")
                continue
            document[cle["nom_cle"]] = valeur
        
        
        if document:
            try:
                collection.insert_one(document)
                print("Document inséré.")
            except Exception as e:
                if  "not authorized" in  e.details.get("errmsg", str(e)).lower():      
                    print("Vous n'avez pas les droits pour ajouter des documents.")
                elif  "duplicate key" in  e.details.get("errmsg", str(e)).lower():      
                        print("Erreur: Critère d'unicité de l'index non respecté ")
                else:
                        print("Erreur mongo :" , e.details.get("errmsg", str(e)) )



