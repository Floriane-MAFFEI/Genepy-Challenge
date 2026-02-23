# Rédige une fonction calculant le périmètre d'un cercle de rayon donné.

# Lise tout d'abord le tutoriel sur les fonctions.

# Ta fonction doit être nommée circle_perimeter, et accepter le paramètre radius, c'est ce paramètre qui recevra le rayon du cercle.

# Ta fonction doit renvoyer le périmètre d'un cercle du rayon donné.

# Pour tester ta fonction, je vais l'essayer avec différentes valeurs, un peu comme :

# >>> circle_perimeter(1)
# 6.283185307179586
# >>> circle_perimeter(10)
# 62.83185307179586
# >>> circle_perimeter(100)
# 628.3185307179587

# Les fonctions
# Par exemple, voici une fonction simple, elle accepte une valeur, qu'elle renvoie directement, sans la modifier :

# def identité(x):
#     return x
# On peut appeler notre fonction identité et vérifier qu'elle renvoie bien la valeur qu'on lui a donné :

# >>> identité(42) == 42
# True
# Ainsi, comparons :

# >>> print(42)
# 42
# et :

# >>> print(identité(42))
# 42
# Les deux se comportent exactement pareil, dans le premier exemple on donne 42 à print qui affiche « 42 », dans le second on donne 42 à identité, qui renvoie 42, qu'on donne directement à print, qui reçoit donc 42, et l'affiche aussi.

# On pourrait aussi comparer :

# >>> quarante_deux = 42
# >>> print(quarante_deux)
# et :

# >>> quarante_deux = identité(42)
# >>> print(quarante_deux)
# ou encore :

# >>> quarante_deux = 42
# >>> quarante_deux = identité(quarante_deux)
# >>> print(quarante_deux)
# qui font aussi, tous, exactement la même chose.

# Astuces
# N'utilise pas print dans ta fonction, elle doit simplement renvoyer le résultat. (https://docs.python.org/fr/3/tutorial/controlflow.html#defining-functions)
# Tu auras besoin d'importer le module math. (https://docs.python.org/fr/3/tutorial/modules.html#standard-modules)(https://docs.python.org/fr/3/library/math.html)
# Tu trouveras PI dans le module math : math.pi (tu peux aussi utiliser math.tau). (https://docs.python.org/fr/3/library/math.html#math.pi)

import math

def circle_perimeter(radius) :
    return 2*radius*math.pi
    

# J'ai testé et re-testé ta fonction, rien à dire, elle fonctionne !