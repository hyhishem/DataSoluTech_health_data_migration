# DataSoluTech: migration des données médicales de patients

## Objectifs

### Sommaire des versions
- V0.1 - Nettoyage de données CSV avec Pandas
- V0.2 - 
- V0.3 -
- V0.4 - 
- V0.5 -

# V0.1 - Nettoyage de données CSV avec Pandas

## Contexte
Ce projet est la première version d'un script de nettoyage et d'analyse de données CSV médicales.  
Il permet de :
- lire un fichier CSV fourni par l'utilisateur ;
- nettoyer les données (formatage des noms, typage des colonnes) ;
- supprimer les doublons ;
- sauvegarder le fichier nettoyé avec le préfixe `clean_`.


## Installation
1. Créer un environnement virtuel :
   ```bash
        $ python3 -m venv .mon_env

   
.mon_env est ajouté à .gitignior pour éviter de surcharger le dossier.

2. Activer l'environnement :
   ```bash
   $ source .mon_env/bin/activate
   ```

3. Installer pandas à partir du fichier requirements.txt
   -Ajouter pandas==2.2.3
   ```bash
   $ source pip install -r requirements.txt
    ```

   
Certains dépandances inutile sont ajouter et  peuvent être retiré. 

## Utilisation

Placer votre fichier CSV dans le même dossier que le script.

Lancer le script après avoir activer l'environement  :
   ```bash
   $ python3 cleaner.py
   ```

Entrer le nom du fichier avec l'extention CSV lorsque le script le demande.

Le fichier nettoyé sera sauvegardé automatiquement sous le nom clean_<nom_du_fichier>.csv.


## Fonctionnalités de cette version

Nettoyage de la colonne Name (mise en Title case) .

Conversion des colonnes Date of Admission et Discharge Date en format date.

Suppression des doublons.

Aperçu des premières lignes et du type des colonnes avant et après nettoyage.

## Remarques

Cette version non automatisé est uniquement basée sur pandas pour le nettoyage .

Les fichiers CSV originaux ne sont pas modifiés. les fichiers nettoyés sont sauvegardés avec le préfixe clean_.



# V0.2 - 



# V0.3 -



# V0.4 -  
