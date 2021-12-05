
'''
Divides the elements into two parts, sorted and unsorted
Check minimum from the unsorted and place it to the sorted area

Space complexity= O(1)
Time compexity= O(n^2)
'''

def InsertionSort(arr):
    i=0
    n=len(arr)
    while i<n:
        min_idx=i
        j=i+1
        while j<n:
            if arr[min_idx]>arr[j]:
                min_idx=j
            j+=1
        if min_idx!=i:
            arr[i],arr[min_idx]=arr[min_idx],arr[i]
        i+=1
    return arr

# print(SelectionSort([7,3,4,6,4,1,5,2]))
assert [1,2,3,4,4,5,6,7]==InsertionSort([7,3,4,6,4,1,5,2])
def bubbleSort(A: list):
    n = len(A)
    unsorted_until_index = n - 1

    for i in range(n):
        swapped = False

        # Last i elements are already in place
        # for j in range(0, n-i-1):
        for j in range(0, unsorted_until_index):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True

        unsorted_until_index -= 1

        # if there is not swapping in the last swap,
        # then the array is already sorted.
        if not swapped:
            break


data = [-2, 45, 0, 11, -9]
bubbleSort(data)

assert data == [-9, -2, 0, 11, 45]