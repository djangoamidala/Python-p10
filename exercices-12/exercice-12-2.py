# exo 12.2
# Créez 4 instances de la classe `User` et affectez les valeurs suivantes à ses attributs :
# - user1
#   - firstname: Joe
#   - lastname: Dalton
#   - email: joe.dalton@example.com
#   - newsletter: true
# - user2
#   - firstname: William
#   - lastname: Dalton
#   - email: william.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: Jack
#   - lastname: Dalton
#   - email: jack.dalton@example.com
#   - newsletter: false
# - user4
#   - firstname: Avrel
#   - lastname: Dalton
#   - email: avrel.dalton@example.com
#   - newsletter: true

# réponse 12.2
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

print(user4.newsletter)