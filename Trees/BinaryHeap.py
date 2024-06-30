# from _typeshed import Self
'''
Heaps are commonly implemented with an array. Any binary tree can be stored in an array, but because a binary heap is always a complete binary tree, it can be stored compactly.
 No space is required for pointers; instead, the parent and children of each node can be found by arithmetic on array indices. 
 These properties make this heap implementation a simple example of an implicit data structure or Ahnentafel list. 
 Details depend on the root position,  which in turn may depend on constraints of a programming language used for implementation, or programmer preference.
 Specifically, sometimes the root is placed at index 1, in order to simplify arithmetic.
 https://en.wikipedia.org/wiki/Binary_heap

 given [0,1,2,3,4,5]

 child =2i+1 and 2i+2
parent at i =(i-1)//2

Search takes O(n) time
Delete n takes O(nlogn) i.e O(n) to find and O(logn) to delete
    
'''


'''
Min Heap
'''
def InsertMinHeap(arr,elem)->None:
    arr.append(elem)
    n=len(arr)-1
    parent=(n-1)//2

    while arr[parent]>arr[n] and parent>=0:
        arr[parent],arr[n]=arr[n],arr[parent]
        n=parent
        parent=(parent-1)//2


'''
Max Heap
'''
def InsertMaxHeap(arr,elem)->None:
    arr.append(elem)
    n=len(arr)-1
    parent=(n-1)//2

    while arr[parent]<arr[n] and parent>=0:
        arr[parent],arr[n]=arr[n],arr[parent]
        n=parent
        parent=(parent-1)//2

# def deleteMaxHeap(arr,elem):
#     i=0
#     deleted=False
#     while i<len(n):
#         if arr[i]==elem:
#             if 2*i+2<len(arr):
#                 if arr[2*i+1]>arr[2*i+2]:
#                     arr[2*i+1],arr[i]=arr[i],arr[2*i+1]
#                     i=2*i+1
#                 else:
#                     arr[2*i+2],arr[i]=arr[i],arr[2*i+2]
#                     i=2*i+2
#             elif 2*i+1<len(arr):
#                 arr[2*i+1],arr[i]=arr[i],arr[2*i+1]
#                 i=2*i+1
#         else:
            
n=[]
InsertMinHeap(n,1)
InsertMinHeap(n,2)
InsertMinHeap(n,3)
InsertMinHeap(n,4)
InsertMinHeap(n,0)

n=[]
InsertMaxHeap(n,1)
InsertMaxHeap(n,4)
InsertMaxHeap(n,3)
InsertMaxHeap(n,5)
InsertMaxHeap(n,0)
InsertMaxHeap(n,9)
InsertMaxHeap(n,6)
# assert [4,3,2,1,0]==n
# in_order(n)
print(n)