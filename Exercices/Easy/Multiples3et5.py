# Rédige un programme qui calcule et affiche la somme de tous les nombres naturels multiples de 3 ou 5 inférieurs à 1000 (< 1000).

# Par exemple, si nous listons tous les nombres multiples de 3 et 5 inférieurs à 20 nous trouverions : 3, 5, 6, 9, 10, 12, 15, 18. La somme de ces nombres donne 78.

# Note que 15 n’est compté qu’une fois.


total = 0

for i in range(1000):  
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(total)

# Joli ! Belle implémentation !!! 💯

