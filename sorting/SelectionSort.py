
'''
Divides the elements into two parts, sorted and unsorted
Check minimum from the unsorted and place it to the sorted area

Space complexity= O(1)
Time compexity= O(n^2)
'''

def SelectionSort(arr):
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
assert [1,2,3,4,4,5,6,7]==SelectionSort([7,3,4,6,4,1,5,2])

