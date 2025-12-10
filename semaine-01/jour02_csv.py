# JOUR 2  : Manipulattioin des fichier CSV

# ============================================
#PARTIE 1 : Creer un fichier CSV manuellement 
# =============================================

# Donnees : Liste de mangas avec leurs info 
mangas_data = [
    ["Titre", "Auteur", "Annee", "Chapitre", "Note"], # Entete
    ["One piece", "Eichiro Oda", 1997, 1100, 9.5],
    ["Naruto", "Masashi Kishimoto", 1999, 700, 9.0],
    ["Attack in Titan", "Hajime Isayama", 2003, 137, 9.8],
    ["Death Note", "Tsugumi Ohba", 2003, 108, 9.2],
    ["My Hero Ademia", "Kohei Horikoshi", 2014, 400, 8.8]
]

# Ecriture dans un fichier CSV
with open("mangas.csv", "w") as f:
    for ligne in mangas_data:
        ligne_csv = ",".join(str(element) for element in ligne)
        f.write(ligne_csv + "\n")
        
print(" Fichier mangas.csv cree! \n")

#==================================
# PARTIE 2 : Lire un fichier CSV
#===================================

# Lecture manuelle

with open("mangas.csv", "r") as f:
    lignes = f.readlines()
    
    entete = lignes[0].strip().split(',')
    print(" ========== En-tete =============")
    print(entete, "\n")
    
    print(" =========== Donnes ============")
    for ligne in lignes[1:]:
        donnee = ligne.strip().split(',')
        print(donnee)
        
        
#===================================================
# PARTIE 3 : Module CSV de Python 
#==================================================

import csv

# Lecture avec le module
print("\n=== LEcture avec le module csv ===")
with open("mangas.csv", "r") as f:
    lecteur = csv.reader(f)
    for ligne in lecteur:
        print(ligne)

        
# Ecriture avec un module csv 
nouveaux_mangas = [
    ["Demon Slayer", "Kyoharu Gotouge", 2016, 205, 9.3],
    ["Jujutsu Kaisen", "Gege Akutami", 2018, 250, 9.1]
]

with open("mangas.csv", "a") as f:
    ecrivain = csv.writer(f)
    for manga in nouveaux_mangas:
        ecrivain.writerow(manga)
        
    
print(" Nouveau mangas ajoutes!")    


# ==========================================
# EXERCICE 3 : Statistique sur les mangas
# ==========================================

# Lecture et Analyse
with open("mangas.csv", "r") as f:
    lecteur = csv.reader(f)
    next(lecteur)   # Sauter l'en-tete (premiere ligne du fichier)
    
    total_chapitre = 0
    total_notes = 0
    nombre_mangas = 0
    mangas_par_annee = {}
    
    for ligne in lecteur:
        titre, auteur, annee, chapitres, note = ligne
        
        annee = int(annee)
        chapitres = int(chapitres)
        note = float(note)
        
        total_chapitre += chapitres
        total_notes += note
        nombre_mangas += 1
        
        # Compteur de decennie
        decennie = (annee // 10) * 10
        mangas_par_annee[decennie] = mangas_par_annee.get(decennie, 0) + 1
        
# Acchicher des statistiques
print("\n" + "="*50)
print(" STATISQUES SUR LES MANGAS")
print("="*50)
print(f"Nombre de mangas : {nombre_mangas}")
print(f"Nombre total de chapitres : {total_chapitre:,}")
print(f"MOyenne de chapitres : {total_chapitre / nombre_mangas:.1f}")
print(f"Note moyenne : {total_notes / nombre_mangas:.2f}/10")
    
print("\n==== Managas par decenie ===")
for decennie in sorted(mangas_par_annee.keys()):
    print(f"{decennie}s : {mangas_par_annee[decennie]} manga(s)") 

with open("statistiques_mangas.txt", "w") as f:
    f.write("STATISTIQUES SUR LES MANGAS\n")
    f.write("="*50 + "\n\n")
    f.write(f"Nombre total : {nombre_mangas}\n")
    f.write(f"Total chapitres : {total_chapitre:,}\n")
    f.write(f"Moyenne chapitres : {total_chapitre / nombre_mangas:.1f}\n")
    f.write(f"Note moyenne : {total_notes / nombre_mangas:.2f}/10\n")

print("\n✓ Statistiques sauvegardées dans statistiques_mangas.txt")   
    
