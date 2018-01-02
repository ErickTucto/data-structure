from BinaryTree.Material import User
from BinaryTree.BST import *

u1 = User(22, "April Mayo")
u2 = User(46, "Diego Diaz")
u3 = User(15, "Carlos Casas")
u4 = User(10, "Juan Muros")
u5 = User(25, "Miluzca Milan")
u6 = User(36, "Erick Tucto")

tree = BST()
tree.insert(u1)
tree.insert(u2)
tree.insert(u3)
tree.insert(u6)
print(tree.right.left.root.full_name)
