import unittest


class Node:
    def __init__(self, val, key):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key


def remove(node):
    node.prev.next = node.next
    node.next.prev = node.prev
    return node.key


class LRUCache:
    
    def __init__(self, capacity):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current_capacity = 0
        self.items = {}

    def put(self, key, val):
        if key in self.items:
            remove(self.items[key])
        
        elif self.current_capacity == self.capacity:
            ky = remove(self.tail.prev)
            del self.items[ky]
        else:
            self.current_capacity += 1
        node = Node(key=key, val=val)
        self.insert(node)
        self.items[key] = node
        # print(val, self.current_capacity, self.capacity)
        
    def insert(self, node):
        if self.head.next != self.tail:
            curr_head = self.head.next
            node.next = curr_head
            curr_head.prev = node
            self.head.next = node
            node.prev = self.head
        else:
            self.head.next = node
            node.prev = self.head
            self.tail.prev = node
            node.next = self.tail
    
    def get(self, key):
        if key in self.items:
            self.put(key, self.items[key].val)
            return self.items[key].val
        else:
            return -1
    
    
obj = LRUCache(capacity=2)

# print(obj.get(key))
# obj.put(key,value)
states = ["put","put","get","put","get","put","get","get","get"]
items = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
for state, item in zip(states,items):
    if state == "put":
        obj.put(item[0], item[1])
    else:
        print(obj.get(item[0]))
