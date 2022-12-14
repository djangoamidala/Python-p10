# exo 6.16
# Ici le but est d'intervertir les éléments de la liste deux à deux
# Liste initiale :
#
#   my_list = [2.71, 42, 123, 2, 3.14, 1.61]
#
# Résultat attendu :
#
#   my_list = [42, 2.71, 2, 123, 1.61, 3.14]

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.16
idx0 = my_list.index(2.71)
idx1 = my_list.index(42)
idx2 = my_list.index(123)
idx3 = my_list.index(2)
idx4 = my_list.index(3.14)
idx5 = my_list.index(1.61)

my_list[idx0],my_list[idx1],my_list[idx2], my_list[idx3],my_list[idx4],my_list[idx5] = my_list[idx1], my_list[idx0], my_list[idx3], my_list[idx2],my_list[idx5],my_list[idx4]

print(my_list)