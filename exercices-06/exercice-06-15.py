# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15

# printing original list 
print("The original list : " + str(my_list))
  
# Extracting length of longest string in list
# using len() + key argument + max()
res = len(max(my_list, key = len))
print("Length of maximum string is : " + str(res))