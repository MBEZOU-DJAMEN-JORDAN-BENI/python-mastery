# compter le nombre de fois ou chaque lettre apparait 

teste = " Je commence enfin mes premier pas dans le python IA pour atteindre mes objectifs de devenir Developpeur IA freelance"
mots = teste.split()
# crer un dictionnaire vide

compteur = {}

# parcourir chaque lettre

for mot in mots:
    if mot not in compteur:
        compteur[mot] = 0
        
    # incrementer le compteur 
    compteur[mot] += 1
    
# afficher le resultat

top_mots = sorted(compteur.items(), key=lambda x : x[1], reverse=True)

print(" ==== Frequence des lettres ======")
for mot, nombre_aparition in top_mots[:5]:
    print(f" La mot '{mot:10}' est presente {nombre_aparition} fois")
    