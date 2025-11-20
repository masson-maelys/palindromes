#### Fonction secondaire
"""Module permettant de vérifier si une chaîne de caractères 
est un palindrome.
"""

def ispalindrome(p):
    """
    Vérifie si une chaîne de caractères est un palindrome.

   
    Args:
        chaine (str): La chaîne de caractères à tester.

    Returns:
        bool: True si la chaîne est un palindrome, False sinon.
    """
    # votre code ici
    trad = str.maketrans("éèëêàùôîç", "eeeeauoic")
    p = (
        p.lower().translate(trad)
        .replace(" ", "")
        .replace(",","")
        .replace("!","")
        .replace("?","")
        .replace("'","")
        .replace(":","")
        .replace("-","")
    )
    inverse = p[::-1]
    return inverse == p

#### Fonction principale


def main():
    """
    Fonction principale de test pour la fonction ispalindrome().

    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
