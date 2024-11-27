def my_sort(lst):
    n = len(lst)  # Longueur de la liste
    coups = 0  # Compteur de coups (échanges)
    
    # Parcourir toute la liste
    for i in range(n):
        swapped = False  # Variable pour suivre si un échange a été effectué lors de ce passage
        
        # Comparer chaque élément avec l'élément suivant jusqu'à l'avant-dernier élément
        for j in range(0, n - i - 1):  # On réduit la plage de comparaison à chaque itération
            if lst[j] > lst[j + 1]:  # Si l'élément courant est plus grand que le suivant
                # Échanger les éléments adjacents
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                coups += 1  # Augmenter le compteur de coups (échanges)
                swapped = True  # Un échange a eu lieu
        
        # Si aucun échange n'a eu lieu, la liste est déjà triée, on peut arrêter
        if not swapped:
            break
    
    # Afficher le nombre total de coups (échanges) nécessaires
    print(f"Nombre de coups nécessaires : {coups}")
    return lst  # Retourner la liste triée

# Exemple d'utilisation
lst = [64, 34, 25, 12, 22, 11, 90]
print("Liste triée :", my_sort(lst))
