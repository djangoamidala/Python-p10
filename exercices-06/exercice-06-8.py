# exo 6.8
# Calculez la somme des nombres de la liste et affichez le résultat

my_list = [2.71, 42]

# réponse 6.8

total = 0
for ele in range(0, len(my_list)):
    total = total + my_list[ele]
print(total)