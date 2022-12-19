# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15
res = len(max(my_list, key = len))
print("Length of maximum string is : " + str(res))

i = 0
while :
    # incrémentation de 1
    i += 1
    print("boucle " + str(i))

    if i == 10:
        # interruption de la boucle
        break