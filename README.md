# DataSoluTech: migration des données médicales de patients (V1.0)

## Context et details

Dans la version précédente V0.1, nous avons développé un script permettant de nettoyer un fichier CSV contenant des données médicales. La V0.2 ajoute une étape : la migration des données nettoyées vers une base MongoDB, avec la possibilité de les visualiser dans Mongo Express. Dans la version V0.3 l'ensemble des services sont conteneurisé sans automatisation.  

Cette version comprend :

1. Un fichier docker-compose.yml avec :
- Python,
    - Installe les dépendances
    - Exécute un script pour créer différents utilisateurs Mongo définis via les variables d'environnement. 
- MongoDB, avec un volume persistant pour stocker les données. 
- Mongo Express pour visualiser et administrer les bases MongoDB via une interface web
- Un réseau pour permettre la communication entre les conteneurs.

2. Un script principal utilisant plusieurs fonctions :  
   - Gestion interactive et automatisée des bases de données et collections MongoDB.  
   - Création et gestion des clés pour structurer les documents.  
   - Nettoyage et transformation des données avant insertion pour garantir la cohérence et l’intégrité
   - Insertion manuelle de documents ou migration automatisée depuis des fichiers CSV.  

## Prérequis
Docker et Docker Compose: installés pour déployer les conteneurs MongoDB, Python et Mongo Express.  


## Authentification et rôles 

Trois comptes sont crées :

- admin pour la gestion complète. Mot de passe admin123
- rw  pour l'ecriture et la lecture.  Mot de passe rw123
- read en lecture seule. Mot de passe read123

L'acces à Mongo Express est possible sur http://localhost:8081

- Identifiant mongo express: admin
- Mot de passe mongo express: pass


## Installation avec Docker et Docker-compose

Pour déployer l'environnement complet avec MongoDB, Mongo Express et le conteneur Python :  

 ```bash
 $ docker-compose up -d
 ```
Cette commande :
- Télécharge les images nécessaires (MongoDB, Mongo Express, Python).
- Crée et démarre les conteneurs dans le réseau défini.
- Monte les volumes pour la persistance des données et le partage des scripts et CSV.
- Exécute automatiquement le script Python pour créer les utilisateurs MongoDB et installer les dépendances.

## Utilisation

Cette version du projet peut être utilisée de deux façons :  

1. Mode automatisé avec arguments

Permet de lancer directement la migration depuis un fichier CSV vers MongoDB :  

 ```bash
 $ docker exec -it python python3 /app/main_script.py --csv /data/dataset.csv --db health_data --collection patients --user rw  --password rw123
 ```
--csv : chemin vers le fichier CSV.

--db : nom de la base MongoDB.

--collection : nom de la collection cible.

--user / --password : identifiants MongoDB.

--pas_vider_col : optionnelle, vide la collection avant insertion par defaut, ajouter pour ne pas vider la collection.


2. Mode interactif via menu:
   
Si tous les arguments essentiels ne sont pas fournis, le script lance un menu interactif permettant :

- De sélectionner ou créer une base et une collection.
- De gérer les clés (ajouter ou visualiser).
- D’insérer des documents manuellement.
- De migrer un fichier CSV après nettoyage.
