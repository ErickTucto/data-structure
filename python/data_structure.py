class List:
    head = None
    size = -1
    class Node():
        next = None
        def __init__(self, book):
            self.book = book

    def preppend(self, book):
        node = self.Node(book)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            head = node
        self.size = self.size + 1
        return True

    def append(self, book):
        node = self.Node(book)
        if self.head == None:
            self.head = node
        else:
            last = self._get(self.size)
            last.next = node
        self.size = self.size + 1
        return True

    def get(self, index):
        node = self._get(index)
        return None if node == None else node.book

    def _get(self, index):
        node = self.head
        if index < 0 or index > self.size:
            return None
        counter = 0
        while counter!=index:
            node = node.next
            counter = counter + 1
        else:
            return node

    def first(self):
        return self.head.book

    def last(self):
        return None if self.head == None else self.get(self.size)

    def insert(self, index, book):
        if index == 0:
            self.preppend(book)
        elif 0 < index <= self.size:
            node = self.Node(book)
            node_temporal = self._get(index - 1)
            node.next = node_temporal.next
            node_temporal.next = node
            self.size = self.size + 1
        else:
            return False
        return True

    def firstDelete(self):
        if self.head == None:
            return False
        self.head = self.head.next
        self.size = self.size - 1
        return True

    def lastDelete(self):
        if self.head == None:
            return False
        return self.delete(self.size)

    def delete(self, index):
        if index == 0:
            return self.firstDelete()
        elif 0 < index <= self.size:
            node_after = self._get(index - 1)
            node_temporal = self._get(index)
            node_after.next = node_temporal.next
            node_temporal.next = None
            self.size = self.size - 1
            return True
        return False

class Queue:
    head = None
    final = None
    class Node:
        def __init__(self, book):
            self.next = None
            self.book = book

    def consult(self):
        return None if self.head == None else self.head.book

    def delete(self):
        if self.head == None:
            return False
        else:
            node_temporal = self.head
            self.head = self.head.next
            node_temporal.next = None
            if self.head == None:
                self.final = self.head
        return True

    def insert(self, book):
        node = self.Node(book)
        if head == None:
            self.head = node
        else:
            self.final.next = node
        self.final = node
        return True
