# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7
idx1 = my_list.index('bar')
idx2 = my_list.index('lorem')
my_list[idx1], my_list[idx2] = my_list[idx2], my_list[idx1]
print(my_list)