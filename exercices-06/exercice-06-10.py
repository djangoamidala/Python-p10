# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10
def Moyenne(l):
    avg = sum(l) / len(l)
    return avg

moyenne = Moyenne(my_list)
print(moyenne)

result = 0
my_sum = 0

for number in my_list:
    my_sum += number
result = my_sum / len(my_list)
print(result)
