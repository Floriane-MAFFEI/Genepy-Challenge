# Rédige un script qui affiche les 10 premières puissances de deux.

# Une par ligne. Attention : pas les nombres carrés !

# Commence à 0, la première puissance de deux est donc 20 (qui vaut un), suivie de 21, 22, jusqu'à 29.

# En Python, l'opérateur « puissance » s'écrit **, donc :

# >>> 2 ** 5
# 32
# Conseils
# Tu auras besoin d'une boucle for pour parcourir un intervalle.

# L’instruction for permet de parcourir les objets contenant d'autres objets. Des chaînes de caractères, des listes, des intervalles sont des objets contenants des objets, tu peux donc utiliser un for pour les parcourir :

# >>> for c in "Hello":
# ...     print("La lettre est :", c)
# ...
# La lettre est : H
# La lettre est : e
# La lettre est : l
# La lettre est : l
# La lettre est : o
# Ou encore :

# >>> for i in [1, 10, 100, 1000]:
# ...     print(i)
# ...
# 1
# 10
# 100
# 1000
# Avec un intervalle :

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
    print(2**i)

# Joli ! C'est juste.

