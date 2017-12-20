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

print("[{}]: [{}]".format(l.get(2).book.title, l.get(2).book.author))
print("[{}]: [{}]".format(l.first().book.title, l.first().book.author))
print("[{}]: [{}]".format(l.last().book.title, l.last().book.author))

print("-"*30)

print("[{}]: [{}]".format(l.get(1).book.title, l.get(1).book.author))
l.insert(
    2,
    Book("Gallinazo sin plumas", "Julio Ramo Ribeyro")
)
print("[{}]: [{}]".format(l.get(1).book.title, l.get(1).book.author))
print("[{}]: [{}]".format(l.get(2).book.title, l.get(2).book.author))

print("-"*30)

l.delete(2)
print("[{}]: [{}]".format(l.get(2).book.title, l.get(2).book.author))

print("-"*30)

l.insert(
    2,
    Book("Gallinazo sin plumas", "Julio Ramo Ribeyro")
)
print("[{}]: [{}]".format(l.last().book.title, l.last().book.author))
l.lastDelete()
print("[{}]: [{}]".format(l.last().book.title, l.last().book.author))

print("-"*30)

l.append(
    Book("Trilce", "Cesar Vallejo")
)
print("[{}]: [{}]".format(l.first().book.title, l.first().book.author))
l.firstDelete()
print("[{}]: [{}]".format(l.first().book.title, l.first().book.author))

print("-"*30)

l.firstDelete()
l.firstDelete()
l.firstDelete()
l.firstDelete()
l.firstDelete()
print(l.get(2))