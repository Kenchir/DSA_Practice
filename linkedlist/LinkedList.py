class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        arr = []
        while self.next is not None:
            arr.append(str(self.data))
            self.next = self.next
        return " -> ".join(arr)
class LinkedList:
    def __init__(self, arr: list):
        head = Node(arr[0])
        tmp = head
        for item in arr[1:]:
            tmp.next = Node(item)
            tmp = tmp.next
        self.head = head

    def __str__(self):
        tmp = self.head
        arr = []
        while tmp is not None:
            arr.append(str(tmp.data))
            tmp = tmp.next
        return " -> ".join(arr)
    
    def delete_mid_node(self, value):
        if self.head is None:
            return self.head
        prev, tmp = self.head, self.head.next
        while tmp is not None:
            if tmp.data == value:
                prev.next = tmp.next
                break
            else:
                prev = tmp
                tmp = tmp.next
            
        