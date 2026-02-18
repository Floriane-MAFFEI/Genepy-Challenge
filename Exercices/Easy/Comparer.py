# Trouve la plus grande valeur cette liste :

# the_list = [
#     143266561,
#     1738152473,
#     312377936,
#     1027708881,
#     1871655963,
#     1495785517,
#     1858250798,
#     1693786723,
#     374455497,
#     430158267,
# ]
# Essaye cet exercice en utilisant uniquement une variable temporaire, une boucle for (https://docs.python.org/fr/3/tutorial/controlflow.html#for-statements), et un if https://docs.python.org/fr/3/tutorial/controlflow.html#if-statements pour comparer les valeurs (https://docs.python.org/fr/3/tutorial/controlflow.html#if-statements).

# Essaye de le faire sans utiliser la fonction max (ni sorted), le but est de s'entraîner avec les mots clefs for et if. En prod, bien sûr, max est le bon outil !!!

the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]

temp = the_list[0]

for i in the_list:
    
    if temp < i :
        temp=i
    
print(temp)

# Bon boulot !!! Belle implémentation !!!! 🥇

