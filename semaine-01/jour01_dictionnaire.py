# Decouvrons le mondes des dictonnaire

# Exercecice note dans un dicitonaire 

note_inf = {
    "inf211": 13,
    "inf221": 16,
    "inf231": 11,
    "inf251": 14
}

note_inf["mat211"] = 12
note_inf["inf211"] = 9

# affficehr une note specifiques
note_inf251 = note_inf.get("inf251", 0)
print(note_inf251)
 
note_inf241 = note_inf.get("inf241", "Ce nest pas votre optionel")
print(note_inf241)
"""
#Afficher toUtes les notes

print("====  NOTES =======")
for matiere, note in note_inf.items():
    print(f"{matiere} : {note}/20")

somme_note = 0

for note in note_inf.values():
    somme_note += note

moyenne = somme_note/len(note_inf)

print(f"La moyene geenrale est {moyenne:.2f}/20")

print(f"Note maximal est {max(note_inf.values())}")

"""