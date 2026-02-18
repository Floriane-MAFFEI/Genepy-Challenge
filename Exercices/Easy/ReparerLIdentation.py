# Il y a un bogue dans le code fourni : l'indentation est absente.

# Ton but ? Le corriger (en ajoutant simplement quatre espaces au bon endroit).

# Le code doit afficher :

# Gonna knock three times:
# *knock*
# *knock*
# *knock*
# - Who's there?
# Qu'est-ce que l'indentation ?
# Tu t’es peut-être posé la question en lisant le code, après le for :

# Comment Python devine ce qui doit être répété ?

# Python ne « devine » pas, c'est à toi de l'indiquer, en ajoutant quatre espaces en début de ligne.

# Chaque ligne indentée (préfixée d'espaces) fait ainsi partie de la « suite » du for, et les lignes qui ne le sont pas n'en font pas partie.

# Exemple :

# for i in range(5):
#     print("Bonjour")
# affiche :

# Bonjour
# Bonjour
# Bonjour
# Bonjour
# Bonjour

print("Gonna knock three times:")
for i in range(3):
    print("*knock*")
print("- Who's there?")

# Bien !! C'est correct ! 🎉

