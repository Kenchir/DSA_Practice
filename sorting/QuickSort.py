

def QuickSort(arr, lo, hi):

    if lo >= hi or lo < 0:
        return   
    
    pi = partition(arr, lo, hi)

    QuickSort(arr, lo, pi-1)
    QuickSort(arr, pi+1, hi)
  
    return arr

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo -1

    for j in range(lo, hi):
         if arr[j] < pivot:
             i += 1
             arr[j], arr[i] = arr[i], arr[j]

    i += 1
    arr[hi], arr[i] = arr[i], arr[hi]
  
    return i
# assert [1, 2, 3, 4, 4, 5, 6, 7]== QuickSort([7,3,4,6,4,1,5,2])

assert [10,30,40,50,70,80,90] == QuickSort([10, 80, 30, 90, 40, 50, 70], 0,6)
assert [1,2,3,4,5,6,7,8,45]==QuickSort([1,45,2,3,4,6,8,5,7] ,0 ,8)
assert [2,31,90,119,125,234,685]==QuickSort([685,119,90,234,2,125,31], 0, 6)