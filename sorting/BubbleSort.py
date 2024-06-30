
'''
Space complexity= O(1)
Time compexity= O(n^2) -Worst
              = O(n) -Best when arr is sorted
''' 

def BubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(i, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        if swapped is False:
            print("sorted")
            return arr
    return arr

print(BubbleSort([8,1,2,3,4,6,5,7]))
assert [1,2,3,4,5,6,7]==BubbleSort([1,2,3,4,6,5,7])
assert [1,2,3,4,5,6,7]==BubbleSort([1,2,3,4,6,5,7])