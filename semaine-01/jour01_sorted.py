# Trier un dictionnaire avec la methode sorted

note_inf = {
    "inf211": 13,
    "inf221": 16,
    "inf231": 11,
    "inf251": 14
}

note_inf["mat211"] = 12
note_inf["inf211"] = 9

note_trie = sorted(note_inf.items(), key=lambda x: x[1], reverse=True)

print("  Les notes sont     ")
for matiere, note in note_trie:
    print(f" {matiere} : {note}/20")