# exo 12.4
# Créez une classe nommée `TaxFreeProduct` qui possède les attributs suivants :
# - _name: valeur par défaut ''
# - _price: valeur par défaut 0.0
# et les méthodes suivantes :
# - __init__() : le constructeur
# - get_name() : renvoie le nom du produit
# - set_name() : détermine le nom du produit
# - get_price() : renvoie le prix du produit
# - set_price() : détermine le prix du produit

# réponse 12.4
class TaxFreeProduct:
    def __init__(self):
        self._name = ''
        self._price = 0.0
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price
    
