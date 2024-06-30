from LinkedList import LinkedList


def remove_duplicates(ll):
    uniqs = set()
    head = ll.head
    uniqs.add(head.data)
    prev, tmp = head, head.next
    while tmp is not None:
        if tmp.data not in uniqs:
            uniqs.add(tmp.data)
            tmp = tmp.next
            prev = prev.next
        else:
            tmp = tmp.next
            prev.next = tmp
    return ll


arr = [2, 2, 3, 5, 4, 5,  6]

ll = LinkedList(arr)
print(ll)

print(remove_duplicates(ll))
ll.delete_mid_node(4)
print(ll)

