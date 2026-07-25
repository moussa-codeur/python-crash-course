# stocke cinq lieux que j'aimerais visiter
locations = ['usa', 'france', 'angleterre', 'canada', 'chine']

# affiche la liste dans son ordre d'origine
print("\naffiche la liste dans son ordre d'origine : ")
print(locations)

# affiche la liste locations par ordre alphabétique sans modifier la liste
print("\naffiche la liste locations par ordre alphabétique sans modifier la liste : ")
print(sorted(locations))

# Montre que la liste est toujours dans son ordre d'origine
print("\nMontre que la liste est toujours dans son ordre d'origine : ")
print(locations)

# affiche la liste dans l'ordre alphabetique inverse sans modifier son ordre
print("\naffiche la liste dans l'ordre alphabetique inverse sans modifier son ordre : ")
print(sorted(locations, reverse = True))

# affiche la liste qui est toujours dans son ordre d'origine
print("\naffiche la liste qui est toujours dans son ordre d'origine : ")
print(locations)

# inverse l'ordre de votre liste avec reverse
print("\ninverse l'ordre de votre liste d'origine : ")
locations.reverse()
print(locations)

# remettre la liste dans son ordre d'origine
locations.reverse()
print("\nremettre la liste dans son ordre d'origine : ")
print(locations)

# utilise sort() pour trier la liste par ordre alphabetique
locations.sort()
print("\naffiche la liste dans l'ordre alphabétique : ")
print(locations)

# modifie la liste dans l'ordre alphabétique inverse
locations.sort(reverse = True)
print("\nmodifie la liste dans l'ordre alphabétique inverse : ")
print(locations)
