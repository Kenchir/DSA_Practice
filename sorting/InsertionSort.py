
'''
Divides the elements into two parts, sorted and unsorted
Check minimum from the unsorted and place it to the sorted area

Space complexity= O(1)
Time compexity= O(n^2)
Best time= O(n) when array is sorted
'''

def InsertionSort(arr):
    i=1
    n=len(arr)
    while i<n:
        if arr[i]<arr[i-1]:
            j=i
            while arr[j]<arr[j-1] and j>0:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                j-=1
        # print(arr)
        i+=1

    return arr

assert [1, 2, 3, 4, 4, 5, 6, 7]== InsertionSort([7,3,4,6,4,1,5,2])
assert [1,2,3,4,5,6,7,8,45]==InsertionSort([1,45,2,3,4,6,8,5,7])
assert [2,31,90,119,125,234,685]==InsertionSort([685,119,90,234,2,125,31])

""""
arr  [8

"""