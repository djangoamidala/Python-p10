# exo 12.3
# Ajoutez chacune des instances de la classe `User` à une liste nommée `users`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom complet et l'email de chaque utilisateur s'il est abonné à la newsletter (c-à-d si newsletter == True)

# réponse 12.3
users = []
class User:
    firstname = ''
    lastname = ''
    email = ''
    newsletter = False
    def __init__(self, firstname, lastname, email, newsletter):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.newsletter = newsletter

user1 = User("Joe","Dalton","joe.dalton@example.com",True)
user2 = User("William","Dalton","william.dalton@example.com",False)
user3 = User("Jack","Dalton","jack.dalton@example.com",False)
user4 = User("Avrel","Dalton","avrel.dalton@example.com",True)


users.append(user1)
users.append(user2)
users.append(user3)
users.append(user4)

for user in users:
    if user.newsletter == True:
        print(f"{user.firstname} {user.lastname} - {user.email}")
