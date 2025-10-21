##########################
#Fonction pour CRUD dans la collection cible
###########################
from pymongo import MongoClient
from datetime import datetime


def crud_collection(db, collection,num_crud,nom_doc=None, age_doc=None, new_nom=None , new_age=None):

##########
# Creer un documents de la collection    
############

        if num_crud=='c':
            try:
                if nom_doc:
                    doc_insertion={'Name':nom_doc, 'Age':age_doc}
                    collection.insert_one(doc_insertion)
                    print(f"Le patient 'Name': {nom_doc} a été ajouté:\n")
                else:
                    print(f"Vous devez specifier le nom du patient:\n")
            except Exception as e:    
                if  "not authorized" in  e.details.get("errmsg", str(e)).lower():      
                    print("Vous n'avez pas les droits pour ajouter des documents.")
                elif  "duplicate key" in  e.details.get("errmsg", str(e)).lower():      
                        print("Erreur: Critère d'unicité de l'index non respecté ")
                else:
                        print("Erreur mongo :" , e.details.get("errmsg", str(e)) )
        
##########
# Afficher un documents de la collection    
############
        elif num_crud=='r':
            doc_nom= list(collection.find({'Name':nom_doc}, {"_id":0}))
            try:
                if nom_doc and doc_nom: 
                    print(f"Résultats de votre recherche sur la clé 'Name': {nom_doc}:\n")
                    for i, doc in enumerate(doc_nom, start=1):
                        print(f"  [{i}] {doc}")
                #if age_doc and doc_age:   
                #    print(f"Résultats de votre recherche sur la clé 'Age': {age_doc}:\n")
                #    for i, doc in enumerate(doc_age, start=1):
                #            print(f"  [{i}] {doc}")
                if not doc_nom:
                    print('Aucun résultat pour cette recherche')
            except Exception as e:    
                if  "not authorized" in  e.details.get("errmsg", str(e)).lower():      
                    print("Vous n'avez pas les droits pour lire des documents.")
                elif  "duplicate key" in  e.details.get("errmsg", str(e)).lower():      
                        print("Erreur: Critère d'unicité de l'index non respecté ")
                else:
                        print("Erreur mongo :" , e.details.get("errmsg", str(e)) )



##########
# Modifier un documents de la collection    
############
        elif num_crud=='u':
            try:
                if new_age:            
                    collection.update_one({"Name":nom_doc, "Age":age_doc},{"$set": {"Age": new_age}})
                    age_doc=new_age
                if new_nom:            
                    collection.update_one({"Name":nom_doc, "Age":age_doc},{"$set": {"Name": new_nom}})                         
            except Exception as e:    
                if  "not authorized" in  e.details.get("errmsg", str(e)).lower():      
                    print("Vous n'avez pas les droits pour modifier des documents.")
                elif  "duplicate key" in  e.details.get("errmsg", str(e)).lower():      
                        print("Erreur: Critère d'unicité de l'index non respecté ")
                else:
                        print("Erreur mongo :" , e.details.get("errmsg", str(e)) )



##########
# Supprimer un documents de la collection    
############
        elif num_crud=='d':
            try:        
                collection.delete_one({"Name":nom_doc, "Age":age_doc}) 
            except Exception as e:    
                if  "not authorized" in  e.details.get("errmsg", str(e)).lower():      
                    print("Vous n'avez pas les droits pour supprimer des documents.")
                elif  "duplicate key" in  e.details.get("errmsg", str(e)).lower():      
                        print("Erreur: Critère d'unicité de l'index non respecté ")
                else:
                        print("Erreur mongo :" , e.details.get("errmsg", str(e)) )


