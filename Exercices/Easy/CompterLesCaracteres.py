# Affiche le nombre de caractères du paragraphe suivant :

# Python is an easy to learn, powerful
# programming language. It has efficient high-level data structures and
# a simple but effective approach to object-oriented
# programming. Python’s elegant syntax and dynamic typing, together with
# its interpreted nature, make it an ideal language for scripting and
# rapid application development in many areas on most platforms.
# J'ai pré-rempli la zone de code avec le paragraphe, sous forme d'une chaîne de caractères (entre guillemets), que j'ai nommé whetting_your_appetite (c'est ce qu'on appelle « une variable »).

# Conseils
# Tu auras besoin de la fonction len, qui peut mesurer quasiment n'importe quoi : des listes, des chaînes de caractères, …

# Si tu es bloqué, tu peux relire le tutoriel sur les chaînes de caractères.

# Tu n'as pas besoin de toucher aux 5 premières lignes, code simplement sous le commentaire # Enter your code below:.

# N'oublie pas d'utiliser la fonction print pour afficher le résultat !

# Qu'est-ce qu'une fonction ?
# Une fonction est quelque chose de nommé, qui prend une (ou plusieurs) valeurs, fait quelque chose avec, et renvoie un résultat.

# Par exemple, la fonction nommée max prend plusieurs valeurs, et renvoie la plus grande de ces valeurs.

# La syntaxe pour lui donner les différentes valeurs est :

# max(1, 5, 2)
# Et, dans ce cas, elle renvoie 5.

# Ce qui est renvoyé par la fonction peut être utilisé :

# En nommant cette valeur (ce qu'on appelle une variable).
# En passant la valeur directement à une autre fonction.
# Typiquement, si tu veux afficher le 5 de l'exemple précédent, tu peux soit faire :

# le_plus_grand = max(1, 5, 2)
# print(le_plus_grand)
# soit:

# print(max(1, 5, 2))

# I prefilled this variable for you, you don't need to touch it.

whetting_your_appetite = """Python is an easy to learn, powerful
programming language. It has efficient high-level data structures and
a simple but effective approach to object-oriented
programming. Python’s elegant syntax and dynamic typing, together with
its interpreted nature, make it an ideal language for scripting and
rapid application development in many areas on most platforms."""

# Enter your code below:
print(len(whetting_your_appetite))

# Super !! Belle implémentation ! 🥇

# C’est plus rapide que compter avec les yeux !

# Ton code affiche :

# 359