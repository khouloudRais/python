def draw_rectangle(width, height):
    # Première et dernière ligne (bord supérieur et inférieur)
    print('-' * width)
    
    # Lignes intermédiaires
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')
    
    # Dernière ligne si la hauteur est supérieure à 1
    if height > 1:
        print('-' * width)

# Exemple d'utilisation
draw_rectangle(10, 3)
