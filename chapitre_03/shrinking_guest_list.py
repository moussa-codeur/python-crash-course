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

print("Boujour chers invités, j' ai une table plus grande.")

# Ajoute de nouveaux invités
guests.insert(0, 'andre weil')
guests.insert(2, 'sankare')
guests.append('ramanujan')

print("\nBonjour " + guests[0].title() + ", je t'invite à diner chez moi.")
print("Bonjour " + guests[1].title() + ", je t'invite à diner chez moi.")
print("Bonjour " + guests[2].title() + ", je t'invite à diner chez moi.")
print("Bonjour " + guests[3].title() + ", je t'invite à diner chez moi.")
print("Bonjour " + guests[4].title() + ", je t'invite à diner chez moi.")
print("Bonjour " + guests[5].title() + ", je t'invite à diner chez moi.")

# Indique que je peux inviter que deux personnes aux dinners
print("\nDésolez, je ne peux inviter que deux personnes aux dîners.")

# Retire le dernier invité puis affiche un message dans la console
pop_guest = guests.pop()
print("\nJe suis désolé " + pop_guest.title() + " de ne plus vous inviter au dîner")
pop_guest = guests.pop()
print("Je suis désolé " + pop_guest.title() + " de ne plus vous inviter au dîner")
pop_guest = guests.pop()
print("Je suis désolé " + pop_guest.title() + " de ne plus vous inviter au dîner")
pop_guest = guests.pop()
print("Je suis désolé " + pop_guest.title() + " de ne plus vous inviter au dîner")

# Affiche un message a chacun des deux qu'ils sont invités
print("\nBonjour " + guests[0].title() + ", je t'invite à diner chez moi.")
print("Bonjour " + guests[1].title() + ", je t'invite à diner chez moi.")


