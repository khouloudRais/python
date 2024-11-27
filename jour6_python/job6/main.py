def note_finale(note):
    # Vérifier si l'étudiant échoue
    if note < 40:
        return f"Échec: la note est de {note}."
    
    # Si l'étudiant a réussi, vérifier l'arrondi
    if note >= 40:
        # Trouver le prochain multiple de 5
        next_multiple_of_5 = ((note // 5) + 1) * 5
        
        # Si la différence entre la note et le prochain multiple de 5 est inférieure à 3, arrondir
        if next_multiple_of_5 - note < 3:
            note = next_multiple_of_5
        return f"Réussite: la note arrondie est de {note}."

# Exemple d'utilisation
print(note_finale(42))  # Note devrait être arrondie à 45
print(note_finale(48))  # Note devrait être arrondie à 50
print(note_finale(37))  # Échec
print(note_finale(73))  # Réussite sans arrondi
