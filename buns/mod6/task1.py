class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0:
            return None
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        return None

    def remove(self, index):
        if index < 0:
            return
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if current and current.next:
            current.next = current.next.next

    def insert(self, index, val):
        if index < 0:
            return
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while current and count < index - 1:
                current = current.next
                count += 1
            if current:
                new_node.next = current.next
                current.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
