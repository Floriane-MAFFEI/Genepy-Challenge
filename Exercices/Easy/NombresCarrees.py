# Rédige un programme qui affiche les 10 premiers nombres carrés, un par ligne.

# Démarre à 0, le premier carré est donc 02 (qui vaut 0), suivi de 12, 22, etc jusqu'à 92.

# Pour rappel, l'opérateur puissance en Python s'écrit **, donc :

# >>> 5 ** 2
# 25
# Conseils
# Tu auras besoin du for pour parcourir un intervalle (range).

# L'instruction for est un outil pour parcourir tout ce qui contient des éléments.

# Les chaînes de caractères, les listes, les intervalles (range) contiennent des éléments.

# Tu peux donc utiliser un for pour les parcourir, exemple :

# >>> for c in "Hello":
# ...     print("La lettre est", c)
# ...
# La lettre est H
# La lettre est e
# La lettre est l
# La lettre est l
# La lettre est o
# Ou :

# >>> for nombre in [1, 10, 100, 1000]:
# ...     print(nombre)
# ...
# 1
# 10
# 100
# 1000
# Ou encore :

# >>> for i in range(10):
# ...     print(i * 2)
# ...
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18

for i in range(10):
    print(i**2)

# Bien joué !!!! C'est correct ! 🙌

# Your code printed:

# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81