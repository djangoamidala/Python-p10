# exo 3.5
# Alice est en vacance et elle veut suivre ses dépenses quotidiennes.
# Stockez le montant de chacune de ses dépenses quotidiennes dans une variable différente :
# - day1 : 26,82
# - day2 : 42,00
# - day3 : 31,41
# - day4 : 63,70
# - day5 : 32,00
# Stockez le nombre de jours dans la variable `days`.
# Calculez le montant total des dépenses en utilisant les variables `day1`, `day2`, etc et stockez le résultat dans la variable `total`.
# Calculez la moyenne des dépenses quotidiennes en utilisant les variables `total` et `days` et stockez le résultat dans la variable `average`.
# Affichez le nombre de jours, le montant total et la moyenne des dépenses.

# réponse 3.5

day1 = 26.82
day2 = 42.00
day3 = 31.41
day4 = 63.70
day5 = 32.00
days = 5
total = day1 + day2 + day3 + day4 + day5 
average = total / days
print(total)
print(average)
print(days)