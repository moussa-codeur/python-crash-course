# Déclare la liste des invités
guests = ['albert einstein', 'cedric villani', 'terence tao'] 
# Affiche les messages d'invitation dans la console
print("Bonjour " + guests[0].title() + ", je t'invite à diner chez moi.")
print("Bonjour " + guests[1].title() + ", je t'invite à diner chez moi.")
print("Bonjour " + guests[2].title() + ", je t'invite à diner chez moi.")

# J' ai choisi une phrase simple polie pour le message
print("\nDésolez, " + guests[0].title() + " ne pourra pas venir.")

# Modifie le premier élément de la liste
guests[0] = 'grigori perelman'

# Affiche les messages d'invitation dans une session terminale
print("\nBonjour " + guests[0].title() + ", je t'invite à diner chez moi.")
print("Bonjour " + guests[1].title() + ", je t'invite à diner chez moi.")
print("Bonjour " + guests[2].title() + ", je t'invite à diner chez moi.")
