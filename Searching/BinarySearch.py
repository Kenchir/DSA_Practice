
'''
Binary search finds a target in a sorted Array
TC=O(logn)
Best case TC= O(1)
SC= O(1)
[1,2,3,4,5,6,7,8]
'''

def binary_search(arr,target):
    n=len(arr)
    start=0
    end=n-1
    while start<=end:
        mid=start+(end-start)//2

        if arr[mid]==target:
            return target
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return -1


# assert(7==binary_search([1,2,3,4,5,6,7,8],8))

print(binary_search([1,2,3,4,5,6,7,8,14,19,121],7.5))