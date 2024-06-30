
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, item):
        if self.head is None:
            self.head = Node(item)
        elif self.head.next is None:
            self.tail = Node(item)
            self.head.next = self.tail
        else:
            node = Node(item)
            self.tail.next = node
            self.tail = node

    def peek(self):
        if self.head is None:
            raise Exception("Empty Queue")
        return self.head.data
    
    def remove(self):
        if self.head is None:
            raise Exception("Empty Queue")
        data = self.head.data
        self.head = self.head.next
        return data
    
    def is_empty(self):
        return self.head == None
        

test = Queue()
test.add(1)
test.add(2)
test.add(3)

assert 1 == test.peek()
assert 1 == test.remove()
assert 2 == test.peek()
assert test.is_empty() is False
test.add(10)
assert 2 == test.remove()
assert 3 == test.remove()
assert 10 == test.remove()
assert test.is_empty() is True

