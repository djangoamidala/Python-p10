# exo 6.13
# Multipliez chacun des nombres dans la liste par 100, réaffactez le résultat à la place de la valeur originelle puis affichez le résultat

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.13
def listMultiply(my_list,n):
    my_list_mult = []
    for x in my_list:
        my_list_mult.append(n*x)  # multiplie la liste par n 
    return my_list_mult
n = 100
print(listMultiply(my_list,n)) # affiche la liste * 100

