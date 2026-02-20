# J’ai rédigé une fonction nommée is_anagram.

# Cette fonction accepte deux paramètres :

# left: qui s’attend à recevoir un mot, sous forme d’une chaîne de caractères,
# right: qui s’attend aussi à recevoir un mot, sous forme d’une chaîne de caractères.
# La fonction doit renvoyer True (vrai) si les deux mots sont des anagrammes entre eux, sinon elle doit renvoyer False (faux).

# Malheureusement j’ai fait une petite erreur dans mon code (tu peux l’envoyer, si tu ne vois pas l’erreur).

# Peux-tu la réparer ?

# Juste au cas où tu aurais un peu trop modifié le code, et aimerais recommencer depuis le début, tu peux copier-coller le code :

# def is_anagram(left, right):
#     left_letters = sorted(left)
#     right_letters = sorted(right)
#     return left_letters = right_letter

def is_anagram(left, right):
    left_letters = sorted(left)
    right_letters = sorted(right)
    return left_letters == right_letters

# Bien joué !! C'est juste !!

