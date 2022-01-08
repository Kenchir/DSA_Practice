'''
Reversing an array in -place
'''

'''
TC = O(n)
SC = O(1)
'''
def reverseArray(arr):

    start, end = 0, len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

print(reverseArray([]))