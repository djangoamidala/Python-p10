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

new_list = []
pos = 0
check = False

for n in my_list:
    if(check == True):
        check = False
        pos += 1
        continue
    n1 = my_list[pos]
    n2 = my_list[pos + 1]
    new_list.append(n2)
    new_list.append(n1)
    check = True
    pos += 1
print(new_list)
print(my_list)
