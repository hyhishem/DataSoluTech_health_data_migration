# DataSoluTech: migration des données médicales de patients (V0.1)

## Details V0.1
La première version est un script de nettoyage du fichier relatives aux données médicales que l'on souhaite faire migrer vers mongodb.  
Le script permet de :
- lire un fichier CSV fourni par l'utilisateur ;
- nettoyer les données (formatage des noms, typage des colonnes) ;
- supprimer les doublons ;
- sauvegarder le fichier nettoyé avec le préfixe `clean_`.

## Prérequis
python3

## Installation
pandas à partir du fichier requirements.txt
   ```bash
   $ pip install -r requirements.txt
   ```
Certains dépandances sont ajouter automatiquement. 

## Utilisation

Placer le fichier avec les données médicales (.CSV) dans le même dossier que le script.

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



