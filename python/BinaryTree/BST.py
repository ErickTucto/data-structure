class BST:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def isLeaf(self):
        return False if self.isBranch() else True

    def isBranch(self):
        return True if self.left != None or self.right != None else False

    def insert(self, user):
        if self.root == None:
            self.root = user
        elif self.root.id < user.id:
            return self._insertRight(user)
        elif self.root.id > user.id:
            return self._insertLeft(user)
        else:
            return False
        return True

    def _insertRight(self, user):
        if self.right == None:
            self.right = BST()
        self.right.insert(user)
        return True

    def _insertLeft(self, user):
        if self.left == None:
            self.left = BST()
        self.left.insert(user)
        return True

    def get(self, id):
        if self.root.id == id:
            return self.root
        elif self.root.id < id:
            return self._getRight(id)
        elif self.root.id > id:
            return self._getLeft(id)
        else:
            return False

    def _getRight(self, id):
        if self.right == None:
            return False
        return self.right.get(id)