# JOUR 2 : Manipulaton des fichiers  en Python

# PARTIE 1 : Ecriture dans un fichier 


# Merthode 1 : Ecriture simple

file = open("first_file.txt", "w") 
file.write(" THE FIRST lINE.  \n")
file.write(" The seconde line. \n")
file.close()    # Important : toujours ferme le fichier

print(" Fichier creer avec succes")

# Methode 2 : Avec "with" (recommande, fermeture automatique)

with open("meilleur_methode.txt", "w") as f:
    f.write(" Cette methode est mieux. \n")
    f.write(" Le fichire se off automatiquement. \n")
    f.write("Meme si ub=ne erreur survient! \n")
    
print(" Deuxieme fichier creer !")

#============================
# Exercie 1 : Liste de mangas
#============================

mes_mangas = [
    "One piece",
    "Naruto",
    "Attack on Titan",
    "Classroom of the Elite",
    "Code Geass"
] 

# Consigne : Ajouter cette liste de mangas dans un fichier ou chaque mangas est sur une seule ligne et en utilisant "with"

with open("mes_mangas.txt", "w") as f:
    f.write(" MA LISTE DE MANGAS \n")
    for manga in mes_mangas:
        f.write(f" {manga} \n") # ou alors f.wirte(manga +"\n")

print(" Ma liste de mangas sauvergardee avec suces !")

#=================================
# PARTIE 2 : Lire depuis un fichier
#=================================

# Methode 1 lire tout le contenu d'un coup

with open("mes_mangas.txt", "r") as f:
    contenu = f.read()
    print("== Contenu Complet ==")
    print(contenu) 

# methode 2 : Lire ligne par (plus efficace pour de gros fichiers)
with open("mes_mangas.txt", "r") as f:
    print("\n === Ligne par Ligne ===")
    for ligne in f:
        ligne_propre = ligne.strip()
        print(f" -{ligne_propre}")
        
# Methode 3 : Lire tout les lignes dans une liste
with open("mes_mangas.txt", "r") as f:
    lignes = f.readlines() #retourne une liste
    print(f"\n === Nombre de mangas : {len(lignes)} ===")
    
    
# ================================
#Exercie 2 : Analyse un texte
# ===============================

# Creer un fichier avec un texte

exemple_texte = """
Python est un language genniale pour data science.
Python permet de manipu;er des donnees facilement.
La data science utilise Python massivement.
L'intellingence artificielle prefere Python aussi
"""

with open("texte_analyse.txt", "w") as f:
    f.write(exemple_texte)
    
#Ton exercice :
#1. Lis ce fichier
#2. Compte la frequence des mots (reutiliser ton code du premiere jours si necessaire)
#3. Sauvegarde les resultats dans "resultats_analyse.txt"

# Lecture du fichier
with open("texte_analyse.txt", "r") as f:
    texte = f.read()

# Analyse de la frequences des mots 

MOTS_VIDES = {"un", "une", "la", "le","les", "des", "l", "pour", "de"}
mots = texte.lower().split()
frequences = {}

for mot in mots:
    mot_propre = mot.strip(".,!?:") # Nettoyre la ponctuation
    if mot_propre and mot_propre not in MOTS_VIDES:
        frequences [mot] = frequences.get(mot_propre, 0) + 1

# Tri des resultats 
top_mots = sorted(frequences.items(), key=lambda x: x[1], reverse = True)

# Sauvegardes des resultats
with open("resultats_analyse.txt", "w") as f:
    f.write("==== RESULTATS DE L'ANALYSE ==== \n")
    for mot, freq in top_mots:
        f.write(f" {mot:20} apparet {freq} fois \n")

print(" Analyse sauvegarder ")    