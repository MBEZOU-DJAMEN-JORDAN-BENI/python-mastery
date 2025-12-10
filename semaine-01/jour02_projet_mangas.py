# PROJET JOUR 2 : Gestion de collection de mangas

import csv
import os

# ================================================
# FONCTION DU PROGRAMME
# ================================================

# Creation du fichier
def create_file():
    if not os.path.exists("collection_mangas.csv"):
        with open("collection_mangas.csv", "w") as f:
            ecrivain = csv.writer(f)
            entete = ["titre", "auteur", "chapitre", "annee", "statut", "note"]
            ecrivain.writerow(entete)
    
    
# Ajout d'un element
def add_manga():   
    print("\n ======= AJOUTER UN MANGAS ======") 
    titre = input("Entrer le titre de l'anime : ")
    auteur = input("Entrer le nom de l'auteur : ")
    chapitre = input("Entrer le nombre de chapitres : ")
    annee = input("Entrer l'annee de la premiere publication : ")
    statut = input(" Statut (En cours/Termine/Abondonne) : ")
    note = input("Entrer la note sur 10 de l'anime : ")
    manga = [titre, auteur, chapitre, annee, statut, note]
    
    with open("collection_mangas.csv", "a") as f:
        ecrivain = csv.writer(f)
        ecrivain.writerow(manga)

    print(f"'{titre}' ajouter a la collection!")

# Afficher la collection
def display_collection():
    print("\n " + "="*70)
    print(" MA COLLECTOIN DE MANGAS")
    print("="*70)
    
    with open("collection_mangas.csv", "r") as f:
        lecteur = csv.reader(f)
        next(lecteur) # Sauter l'en tete
        
        for i, ligne in enumerate(lecteur, 1):
            titre, auteur, chapitres, annee, statut, note = ligne
            print(f"\n {i}. {titre}")
            print(f" Auteur : {auteur}")
            print(f" Annee : {annee}")
            print(f" Statut: {statut} | Nombre de chapitres : {chapitres} | Note : {note}/10")
            
        
# Statistique        
def statistiques():
    total_chapitres = 0
    total_notes = 0
    nombre_mangas = 0
    statuts = {}
    with open("collection_mangas.csv", "r") as f:
        lecteur = csv.reader(f)
        next(lecteur)
        
        for ligne in lecteur:
            titre, auteur, chapitres, annee, statut, note = ligne
            try:
                total_chapitres += int(chapitres)
                total_notes += float(note)
                nombre_mangas += 1
                statuts[statut]  = statuts.get(statut, 0) + 1
            except:
                print(f" Donnees de '{titre}' incorecte verifier les informations entrez!")
                continue 
            
    if nombre_mangas > 0:
        print("\n" + "="*50)
        print("STATISTIQUES")
        print("="*50)
        print(f"Nombre de mangas : {nombre_mangas}")
        print(f"Chapitres lus au total : {total_chapitres:,}")
        print(f"Note moyenne : {total_notes / nombre_mangas:.2f}/10")
        
        print("\nRépartition par statut :")
        for statut, nombre in statuts.items():
            print(f"  - {statut} : {nombre}")
    else:
        print("\n Aucun mangas present ans la liste!")
        

# ========================================
# MENU PRINCIPAL
# ========================================

def menu():
    create_file()
    
    while True:
        print("\n" + "="*50)
        print("GESTIONNAIRE DE COLLECTION DE MANGAS")
        print("="*50)
        print("1. Ajouter un manga")
        print("2. Voir ma collection")
        print("3. Voir les statistiques")
        print("4. Quitter")
        
        choix = input("\nChoisis une option (1-4) : ")
        
        if choix == "1":
            add_manga()
        elif choix == "2":
            display_collection()
        elif choix == "3":
            statistiques()
        elif choix == "4":
            print("\nÀ bientôt! ")
            break
        else:
            print(" Choix invalide!")

# Lancement du programme 
if __name__ == "__main__":
    menu()        
        