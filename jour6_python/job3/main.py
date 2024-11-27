def draw_carpet(n):
    # Afficher la première ligne de plus (+) (bordure supérieure)
    print('+' + '-' * (n + 1) + '+')  # Bordure avec "+" (1 pour la gauche, 1 pour la droite et n+1 pour les colonnes)
    
    # Parcours chaque ligne du tapis
    for i in range(n + 1):
        # Commence par une bordure à gauche "|"
        line = "|"
        
        # Crée chaque ligne du tapis avec une diagonale
        for j in range(n + 1):
            if i == j:
                line += " "  # Diagonale
            else:
                line += "."  # Espaces vides

        # Ajoute la bordure à droite "|" et affiche la ligne
        line += "|"
        print(line)

    # Afficher la dernière ligne de plus (+) (bordure inférieure)
    print('+' + '-' * (n + 1) + '+')

# Exemple d'utilisation
draw_carpet(10)

