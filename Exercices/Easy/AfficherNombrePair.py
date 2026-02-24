# Implémente une fonction affichant tous les nombres pairs dans l’intervalle demandé, un nombre par ligne.

# Ta fonction doit se nommer print_even_numbers et accepter deux paramètres : start et stop.

# Tout comme la fonction range de Python, qui produit des intervalles, ta fonction doit commencer par chercher des nombres pairs incluant start mais excluant stop, rappelle-toi :

# for i in range(0, 10):
#     print(i)
# donne :

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Je veux que print_even_numbers(0, 10) affiche :

# 0
# 2
# 4
# 6
# 8
# Astuces
# Tu peux utiliser le reste de la division entière par 2 pour savoir si un nombre est pair ou impair. En Python c’est l’opérateur % qu’on utilise pour obtenir le reste de la division entière :

# >>> 2 % 2
# 0
# >>> 3 % 2
# 1
# >>> 4 % 2
# 0
# >>> 5 % 2
# 1
# >>> 6 % 2
# 0
# Si le reste vaut 1, le nombre est impair, s’il vaut 0 le nombre est pair.

# Tu auras donc besoin d’un if et d’un print.

def print_even_numbers(start, stop):
    for i in range(start,stop):
        if(i%2==0):
            print(i)

# Nicely done! I love even numbers!

