


# def solution(nums, target):
#
#     res = []
#
#     def backtrack_call()
#


def bubble_sort(arr):
    
    i = 0
    n = len(arr)
    
    while i < n:
        j = i
        
        while j < n - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
            
        i += 1
    return arr

print(bubble_sort([7,3,4,6,4,1,5,2]))
assert [1, 2, 3, 4, 4, 5, 6, 7]== bubble_sort([7,3,4,6,4,1,5,2])

