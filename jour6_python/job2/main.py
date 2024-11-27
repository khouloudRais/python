def draw_triangle(height):
    # Parcourir chaque ligne de 1 à height (inclus)
    for i in range(1, height + 1):
        # Calculer le nombre d'espaces avant le premier "/"
        spaces = " " * (height - i)
        
        if i == height:
            # La dernière ligne, on met des "_" pour la base
            line = "/" + "_" * (2 * i - 3) + "\\"
        else:
            # Pour les autres lignes, on met "/" et "\"
            line = "/" + " " * (2 * i - 3) + "\\"
        
        # Afficher la ligne avec les espaces et les symboles
        print(spaces + line)

# Exemple d'utilisation
draw_triangle(3)
