from LinkedList import LinkedList, Node


def sum_linked_list(l1: LinkedList, l2:LinkedList):
    
    l1, l2 = l1.head, l2.head
    carry = 0
    head = None
    p = LinkedList()
    while l1 is not None and l2 is not None:
        
        t = l1.data + l2.data + carry
        if t >= 10:
            t = t - 10
            carry = 1
        else:
            carry = 0
        if head is None:
            head = Node(t)
            p = head
            head = head.next
        else:
            head.next = Node(t)
            head = head.next
        print(p)
        l1 = l1.next
        l2 = l2.next
        
    while l1 is not None:
        t = l1.data + carry
        if t > 10:
            carry = 1
            t = t - 10
        else:
            carry = 0
        head.next = Node(t)
        head = head.next
        l1 = l1.next
    
    while l2 is not None:
        t = l2.data + carry
        if t > 10:
            carry = 1
            t = t - 10
        else:
            carry = 0
            
        head.next = Node(t)
        head = head.next
        l2 = l2.next
        
    return p

arr1, arr2  = LinkedList([7, 1, 6]), LinkedList([5, 9, 2])

ll = sum_linked_list(arr1, arr2)
print(type(ll), type(arr1))

print((ll))




"""
 arr = [s, b, c ,d]
  a -> b -> c ->d
  prev curr
  a     b
  b     c
  c     d
  
 """