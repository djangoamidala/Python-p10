import random
# int(foo) rend un nombre entier
# foo-a donne le coté décimal
foo = 2.71 
a = int(foo)
b = foo - a
print(a, b)

# Random.uniform donne aléatoirement entre 1 et 1000 
# format(.2f) donne 2 après la virgule
d = random.uniform(1, 1000)
print(format(d, '.2f'))