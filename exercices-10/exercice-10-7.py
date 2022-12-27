# exo 10.7
# Créer une fonction nommée `compute_tax()` qui :
# - prend un paramètre nommé `price` de type `float`
# - prend un paramètre nommé `tax_type` de type `int`
# - ajoute une taxe de 2,1 % à `price` si `tax_type` est égal à `1`
# - ajoute une taxe de 5,5 % à `price` si `tax_type` est égal à `2`
# - ajoute une taxe de 10 % à `price` si `tax_type` est égal à `3`
# - ajoute une taxe de 20 % à `price` si `tax_type` est égal à `4`
# - renvoie le prix initial si `tax_type` n'est pas reconnu
# Appelez la fonction et affichez le résultat avec un montant de 100 € pour chaque type de taxe
#
# Référence : [Quels sont les taux de TVA en vigueur en France et dans l'Union européenne ? | economie.gouv.fr](https://www.economie.gouv.fr/cedef/taux-tva-france-et-union-europeenne)

# réponse 10.7
def compute_tax(price:float, tax_type:int):
    if tax_type == 1:
        price += price * 2.1 / 100 
    if tax_type == 2:
        price += price * 5.5 / 100
    if tax_type == 3:
        price += price * 10 / 100
    if tax_type == 4:
        price += price * 20 / 100
    return price

print(compute_tax(100,1))
print(compute_tax(100,2))
print(compute_tax(100,3))
print(compute_tax(100,4))