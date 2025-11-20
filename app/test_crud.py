import pytest
import mongomock
from def_crud_collection import crud_collection

def test_crud():
    # Créer une base simulée
    client = mongomock.MongoClient()
    db = client["test_db"]
    collection=db["users"]

    # Ajouter un document
    crud_collection(db, collection, 'c', "Alice", 25)

    # Vérifier l'ajout
    result = collection.find_one({"Name": "Alice"})
    assert result is not None
    assert result["Name"] == "Alice"
    assert result["Age"] == 25

    # Mettre à jour le document
    crud_collection(db, collection, 'u', "Alice", 25, "Bob", 26)

    # Vérifier la mise à jour
    result = collection.find_one({"Name": "Bob"})
    assert result is not None
    assert result["Name"] == "Bob"
    assert result["Age"] == 26
