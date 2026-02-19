# Rédige un script affichant le nombre de mots dans le paragraphe suivant :

# Python is an easy to learn, powerful programming language. It has efficient high level data structures and a simple but effective approach to object oriented programming. This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. For a description of standard objects and modules...

# J'ai pré-rempli l'éditeur de code avec le paragraphe, assigné à une variable, en cas de souci tu peux re-commencer à partir d'un copié-collé :

# whetting_your_appetite = "Python is an easy to learn, powerful programming language. It has efficient high level data structures and a simple but effective approach to object oriented programming. This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. For a description of standard objects and modules..."

# Conseils
# Jette un œil à la méthode split.

#!/usr/bin/env python3

whetting_your_appetite = "Python is an easy to learn, powerful programming language. It has efficient high level data structures and a simple but effective approach to object oriented programming. This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. For a description of standard objects and modules..."

# Enter your code below:
array=whetting_your_appetite.split(" ")

print(len(array))

# Yes, there's 52 words in this paragraph, nicely done!