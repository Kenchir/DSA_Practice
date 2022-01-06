# from _typeshed import Self
'''

'''

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        pass

def insert(root,data)->None:

    if root is None:
        root=Node(data)

    elif data < root.data:
        if root.left is None:
            root.left = Node(data)

        else:

            insert(root.left,data)
    else:
        if root.right is None:
            root.right = Node(data)

        else:
            insert(root.right,data)
'''
Returns the node with largest item from a given root
'''
def findLargest(root):
    if root.right is not None:
        return findLargest(root.right)
    else:
        return root
    
'''
    Deleting:
    1.  leaf node
    2.  with one child
    3.  has 2 children
'''
def delete(root,item):
    if root is None:
        return -1
    elif root.data==item:
        #No child
        if root.left is None and root.right is None:
            root=None
        #Child on right
        elif root.left is None:
            temp=root.right
            root.right=None
            root.data=temp.data
        #Child on left
        elif root.right is None:
            temp=root.left
            root.left=None
            root.data=temp.data
        #Both Children
        else:
            temp=findLargest(root.left)
            root.data=temp.data
            root.left=delete(root.left,temp.data)

    elif item < root.data:
        root.left= delete(root.left,item)

    elif item > root.data:
        root.right= delete(root.right,item)
    
    return root
'''
Search a given Item in Binary tree
return item if found
return -1 not found
'''
def search(root,item):
    if root is None:
        return -1
    elif item == root.data:
        return item
    elif item > root.data:
        return search(root.right,item)
    else:
        return search(root.left,item)

def in_order(root):

    if root is not None:
        in_order(root.left)
        print(root.data)
        in_order(root.right)

def pre_order(root):

    if root is not None:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    
    if root is not None:
        post_order(root.left)
        post_order(root.right)
        print(root.data)

def is_binary_tree(root):
    if root is not None:
        left, right= root.left, root.right

        if left is not None and root.data > left.data:
            is_binary_tree(left)

        
        if right is not None and root.data < right.data:
            is_binary_tree(right)
        
        return False
        
    return True



n=Node(5)

insert(n,3)
insert(n,4)
insert(n,1)
insert(n,2)
insert(n,8)
insert(n,6)
insert(n,7)

# in_order(n)

n=delete(n,3)
in_order(n)
assert search(n,7)==7