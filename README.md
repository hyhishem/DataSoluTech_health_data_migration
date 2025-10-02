# DataSoluTech: migration des données médicales de patients (V0.2)

## Context et details V0.2
Dans la version précédente (V0.1), nous avons développé un script permettant de nettoyer un fichier CSV contenant des données médicales.
La V0.2 ajoute une étape : la migration des données nettoyées vers une base MongoDB, avec la possibilité de les visualiser dans Mongo Express.

Cette version comprend :

1. un script Python pour
- nettoyer les données avec pandas (V0.1)
- transférer les données dans MongoDB.

2. un fichier docker-compose.yml qui déploie :
- MongoDB
- Mongo Express (interface graphique web pour MongoDB)

## Prérequis
python3
pip
Docker et Docker Compose 


## Installation
### Python

Installer les dépendances nécessaires :

 ```bash
 $ pip install -r requirements.txt
 ```
   
### Côté Docker

Lancer les services MongoDB et Mongo Express avec :

 ```bash
 $ docker-compose up -d
 ```


## Utilisation

Placer le fichier CSV à migrer dans le même dossier que le script Python.

Lancer le script :

 ```bash
 $ python3 main_script.py
 ```

Le script effectuera :

- le nettoyage des données (comme en V0.1) 
- quelques operations CRUD
- la migration  dans MongoDB (health_data.patients)

Mongo Express est accessible sur http://localhost:8081

Identifiant mongo express: admin
Mot de passe mongo express: pass


## Fonctionnalités de cette version

- Nettoyer les données avec pandas (hérité de la V0.1)
- Connexion à MongoDB via pymongo
- Création de la base health_data et de la collection patients
- Operations CRUD 
- Insertion des documents issus du fichier nettoyé
- Interface Mongo Express pour visualiser et interroger les données

## Remarques

Cette version permet d’avoir un premier flux complet (CSV - Nettoyage - MongoDB - Visualisation) 

Les identifiants par défaut (admin/admin123  et admin/pass) sont uniquement utilisés pour le développement local. Pour un déploiement réel, il est recommandé de renforcer la sécurité (authentification, rôles, mot de passe fort). 

En ce qui concerne la structure du script, il serait pertinent de l’organiser en plusieurs fonctions pour le rendre plus lisible, réutilisable et résilient.


