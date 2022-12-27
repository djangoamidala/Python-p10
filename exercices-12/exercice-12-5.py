# exo 12.5
# Créez 3 instances de la classe `TaxFreeProduct` et affectez les valeurs suivantes à ses attributs en utilisant les setters :
# - product1
#   - name: Foo
#   - price: 31,41
# - product2
#   - name: Bar
#   - price: 27,18
# - product3
#   - name: Baz
#   - price: 16,18

# réponse 12.5
class TaxFreeProduct:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

product1 = TaxFreeProduct("Foo", 31.41)

product2 = TaxFreeProduct("Bar", 27.18)

product3 = TaxFreeProduct("Baz", 16.18)

print(product1.name, product1.price)