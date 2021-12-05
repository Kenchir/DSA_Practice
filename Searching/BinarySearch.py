
'''
Binary search finds a target in a sorted Array
TC=O(logn)
SC= O(1)
[1,2,3,4,5,6,7,8]
'''

def binary_search(arr,target):
    n=len(arr)

    if target==arr[0]:
        return 0
    if target==arr[n-1]:
        return n-1
    middle=n//2
    while middle>0 and middle<n-1:
        if arr[middle]==target:
            return middle
        else:
            if arr[middle]>target:
                middle=middle//2
                print(middle)
            else:
                middle=(n-middle)//2+middle
    return -1


# assert(7==binary_search([1,2,3,4,5,6,7,8],8))

print(binary_search([1,2,3,4,5,6,7,8],7))