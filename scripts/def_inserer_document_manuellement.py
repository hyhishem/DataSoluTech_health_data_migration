from pymongo import MongoClient
from datetime import datetime


def inserer_document_manuellement(db, collection):
    cles = list(db["cles"].find({}, {"_id":0}))
    if not cles:
        print("Aucune clé disponible.")
        return
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
                elif cle["type_cle"]=="date":
                    valeur = datetime.strptime(valeur, "%Y-%m-%d")
            except ValueError:
                print(f"\n Valeur invalide pour '{cle['nom_cle']}', ignorée.")
                continue
            document[cle["nom_cle"]] = valeur
        if document:
            try:
                collection.insert_one(document)
                print("Document inséré.")
            except Exception as e:
                if  "not authorized" in  e.details.get("errmsg", str(e)).lower():      
                    print("Vous n'avez pas les droits pour ajouter des documents.")
                else:
                    print("Erreur mongo")



