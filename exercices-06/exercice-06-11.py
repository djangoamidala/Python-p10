# exo 6.11
# Trouvez l'index de la valeur `3.14` dans la liste et affichez le résultat
# Note : faites une boucle et n'utilisez pas la méthode `index()`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]


# réponse 6.11
target = 3.14

for i in range(len(my_list)):
  if my_list[i] == target:
   print(f"{target} found at index {i}")