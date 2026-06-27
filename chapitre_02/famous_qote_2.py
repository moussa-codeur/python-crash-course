# Ce programme affiche une citation d' Albert Einstein 
# en utilisant les concaténations sur les chaînes de caractères.

# Données
famous_person = "albert einstein"
qote = "\"A person who never made a mistake never tried anything new.\""

# Nettoie et formate les données
famous_person = famous_person.strip()
qote = qote.strip()

message = famous_person.title() + " once said, " + qote
print(message)
