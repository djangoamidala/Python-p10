# exo 5.1
# Ajoutez de la documentation à la fonction suivante et vérifiez
# qu'elle s'affiche correctement en utilisant la fonction help()

# réponse 5.1
def  multiplication (a: float, b: float) -> float:
    '''a and b float'''
    return a * b
print(multiplication.__doc__)
print(help(multiplication))