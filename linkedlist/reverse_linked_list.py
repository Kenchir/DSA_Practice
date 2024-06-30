

def reverse_linked_list(ll):
    head = ll.head
    curr = head
    prev = head
    head = head.next
    
    while head is not None:
        curr = head
        curr.next = prev
        prev = curr
        head = head.next
        

"""
 arr = [s, b, c ,d]
  a -> b -> c ->d
  prev curr
  a     b
  b     c
  c     d
  
 """