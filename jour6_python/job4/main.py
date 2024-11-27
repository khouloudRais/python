def caesar_cipher(message, shift):
    result = ""
    
    # Parcours chaque caractère du message
    for char in message:
        if char.isalpha():  # Si c'est une lettre
            # Déterminer si la lettre est en majuscule ou minuscule
            start = ord('A') if char.isupper() else ord('a')
            
            # Appliquer le décalage
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result += new_char
        else:
            # Si ce n'est pas une lettre, on l'ajoute tel quel
            result += char
    
    return result

# Exemple d'utilisation
message = "Bonjour, c'est un message secret!"
shift = 3
print(caesar_cipher(message, shift))  # Chiffrement vers la droite avec un décalage de 3
