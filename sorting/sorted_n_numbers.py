

def sort(arr):
    i, n = 0, len(arr) - 1
    sorts = 0
    while sorts <= n and i <= n:
        print(arr, i, sorts, arr[i])
        if i != arr[i] - 1:
            item = arr[i]
            arr[i], arr[item - 1] = arr[item - 1], item
            sorts += 1
        else:
            i += 1
    print(arr)
    return arr



assert [1,2,3,4,5,6,7] == sort([7,3,6,4,1,5,2])
assert [1, 2, 2, 3, 4] == sort([1,3,4,2,2])
