
"""
Stack Using Array
"""


class MyStack:
    def __init__(self):
        self.stack = []
        self.items = 0
    
    def pop(self):
        if self.items == 0:
            raise Exception("Empty stack")
        self.items -= 1
        return self.stack.pop()
    
    def is_empty(self):
        return self.items == 0
    
    def peek(self):
        return self.stack[-1]
    
    def push(self, item):
        self.items += 1
        self.stack = self.stack.append(item)
        

class Node:
    def __init__(self, data):
        self.head = data
        self.next = None
        self.min = data


class StackL:
    def __init__(self):
        self.stack = Node(None)
    
    def pop(self):
        if self.stack.head is None:
            raise Exception("Empty stack")
        head = self.stack
        next_ = self.stack.next
        self.stack = next_
        return head.head
     
    def is_empty(self):
        return self.stack.head is None
    
    def peek(self):
        if self.stack.head is None:
            raise Exception("Empty stack")
        return self.stack.head
    
    def push(self, item):
        node = Node(item)
        if not self.is_empty():
            if item < self.stack.min:
                node.min = item
            else:
                node.min = self.stack.min
        else:
            node.min = item
        node.next = self.stack
        self.stack = node
    
    def min(self):
        if self.is_empty():
            raise Exception("Empty Stack")
        return  self.stack.min
    
    

"""
1,2,3,10
1,2,3
1,2,3,0
"""

test = StackL()
test.push(1)
test.push(2)
test.push(3)
test.push(10)

assert 10 == test.peek()
assert 1 == test.min()
assert 10 == test.pop()
assert 3 == test.peek()
test.push(0)
assert test.is_empty() is False
assert 0 == test.min()
test.pop()
test.pop()
assert 1 == test.min()
test.pop()
assert 1 == test.peek()
test.pop()
assert True == test.is_empty()


def sort_stack(stack: StackL):
    if stack.is_empty():
        return stack
    

    def sss():
        return  1, 2



