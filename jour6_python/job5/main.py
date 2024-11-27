def distance_parcourue_par_semaine(marches, hauteur_marche):
    # Calcul de la distance parcourue en cm pour une descente et remontée
    distance_par_jour_cm = 5 * 2 * marches * hauteur_marche
    
    # Calcul de la distance parcourue en cm sur une semaine (7 jours)
    distance_par_semaine_cm = distance_par_jour_cm * 7
    
    # Conversion en mètres
    distance_par_semaine_m = distance_par_semaine_cm / 100
    
    # Affichage du résultat
    print(f"Pour {marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_par_semaine_m:.2f} m par semaine.")

# Exemple d'utilisation
distance_parcourue_par_semaine(100, 20)  # 100 marches de 20 cm
