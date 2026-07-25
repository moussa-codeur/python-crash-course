langages = ['wolof', 'français', 'anglais', 'arabe', 'serere', 'puular']

# trie la liste par ordre alphabetique sans modifier l'ordre d'origine
print("affiche la liste triée sans modifier la liste d'origine")
print(sorted(langages))

# affiche la liste par ordre alphabétique inverse sans modifier la liste initiale
print("\naffiche la liste par ordre alphabétique inverse sans modifier la liste initiale")
print(sorted(langages, reverse = True))

# inverse l'ordre de la liste originale 
print("\naffiche la liste inversé")
langages.reverse()
print(langages)

# remettre la liste dans son ordre orginal
print("\naffiche la liste dans son ordre initial")
langages.reverse()
print(langages)

# trie la liste par ordre alphabétique croissant 
print("\ntrie et affiche la liste par ordre croissant")
langages.sort()
print(langages)

# trie la liste par ordre décroissant
print("\ntrie la liste par ordre alphabétique décroissant et l'affiche")
langages.sort(reverse = True)
print(langages)

# affiche le nombre d'éléments de la liste
print("\nle nombre d'élément de la liste est : ")
print(len(langages))
