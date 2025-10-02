#!/usr/bin/env python3

import pandas as pd

########################
#Demande du fichier
########################

dataset = input("Entrez le nom du fichier CSV: ").strip()

df = pd.read_csv(dataset)
print("\n \n Aperçu des premières lignes")
print(df.head())


print("\n \n Aperçu du types des colonnes")
print(df.dtypes)



################################################
#nettoyage et modification du type des colonnes  (Version manuelle)
################################################

df['Name']=df['Name'].str.title()  # Majuscule uniquement en debut pour uniformiser 

df['Billing Amount']=df['Billing Amount'].round(2) # Prendre uniquement deux decimales

df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], format='%Y-%m-%d') # Format date 
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'], format='%Y-%m-%d') # Format date 

#############################
#Suppression des doublons 
##############################
lignes_avant = len(df) #  Nombre de lignes avant de supprimer les doublons
df = df.drop_duplicates() # Suppression des doublons
df=df[~df[['Name' ,'Date of Admission', 'Discharge Date', 'Room Number']].duplicated()] # Suppression des doublons partiel non probable 
lignes_apres = len(df)  #  Nombre de lignes après avoir supprimer les doublons

print(f" \n \n {lignes_avant - lignes_apres} doublons ont été supprimés")


####################################
#Sauvegarde du fichier nettoyé 
####################################

output_file = "clean_" + dataset   # Ajout d'un préfix pour definir le nom du fichier nettoyer 

df.to_csv(output_file, index=False)
print(f"\n\nLes données nettoyées sont sauvegardées dans '{output_file}'")

######################
# Aperçu final 
######################

print("\n \nAperçu final \n \n:") #Visuel après nettoyage
print("\n \n Aperçu des premières lignes")  
print(df.head())


print("\n \n Aperçu du types des colonnes")
print(df.dtypes)
