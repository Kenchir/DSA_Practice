"""
4.2 Minimal Tree:
 Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
 
 [1,2,3,4,5,6]
 
 approch - middle of each sub array becomes the root
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def minimal_tree(arr: list, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # print(mid)
    root = Node(arr[mid])
    
    root.left = minimal_tree(arr, start, mid - 1)
    root.right = minimal_tree(arr, mid + 1, end)
    
    return root
    

arr = []
def print_tree(root):
    if root is not None:
        arr.append(root.data)
        print_tree(root.left)
        print_tree(root.right)
    print(arr)
tree = minimal_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 9)

(tree)
    
    