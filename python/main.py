from book import Book
from data_structure import *

l = List()
l.append(
    Book("El caballero Carmelo", "Abraham Valdelomar")
)
l.append(
    Book("Oliver Twist", "Charles Dickens")
)
l.append(
    Book("Trilce", "Cesar Vallejo")
)

print("[{}]: [{}]".format(l.get(2).title, l.get(2).author))
print("[{}]: [{}]".format(l.first().title, l.first().author))
print("[{}]: [{}]".format(l.last().title, l.last().author))

print("-"*30)

print("[{}]: [{}]".format(l.get(1).title, l.get(1).author))
l.insert(
    2,
    Book("Gallinazo sin plumas", "Julio Ramo Ribeyro")
)
print("[{}]: [{}]".format(l.get(1).title, l.get(1).author))
print("[{}]: [{}]".format(l.get(2).title, l.get(2).author))

print("-"*30)

l.delete(2)
print("[{}]: [{}]".format(l.get(2).title, l.get(2).author))

print("-"*30)

l.insert(
    2,
    Book("Gallinazo sin plumas", "Julio Ramo Ribeyro")
)
print("[{}]: [{}]".format(l.last().title, l.last().author))
l.lastDelete()
print("[{}]: [{}]".format(l.last().title, l.last().author))

print("-"*30)

l.append(
    Book("Trilce", "Cesar Vallejo")
)
print("[{}]: [{}]".format(l.first().title, l.first().author))
l.firstDelete()
print("[{}]: [{}]".format(l.first().title, l.first().author))

print("-"*30)

l.firstDelete()
l.firstDelete()
l.firstDelete()
l.firstDelete()
l.firstDelete()
print(l.get(2))