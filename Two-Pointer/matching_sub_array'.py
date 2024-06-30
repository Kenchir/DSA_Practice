import sys


def sub_array(arr, k):
    n = len(arr)
    max_sum = 0
    current_sum = arr[0]
    left, right = 0 ,1
    tmp = k
    while right < n:
        if right - left < k:
            current_sum += arr[right]
            right += 1
        else:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[left]
            left += 1
            
    return  max(max_sum, current_sum)
    

assert  39 == sub_array([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
assert  700 == sub_array([100, 200, 300, 400], 2)


def smallest_sub_arr(arr, s):
    min_size = sys.maxsize
    curr_sum = arr[0]
    min_start = 0
    i = 1
    
    while i < len(arr):
        curr_sum = arr[i]
        if curr_sum >= s:
            return [arr[i]]
        
        j = i + 1
        while j < len(arr):
            curr_sum += arr[j]
            if curr_sum > s:
                if j - i < min_size:
                    min_size = j - i
                    min_start = i
                break
            else:
                j += 1
        
        i += 1
    # print(arr[min_start: min_start + min_size + 1])
    return arr[min_start: min_start + min_size + 1]
    
    
    
    


assert [4, 45, 6] == smallest_sub_arr([1, 4, 45, 6, 0, 19], 51)


def smallest_sub_arr_v2(arr, s):
    min_size = sys.maxsize
    curr_sum = arr[0]
    min_start = 0
    i, j = 0, 1
    n = len(arr)
    if curr_sum == s:
        return [arr[i]]
    while i < n and j < n:
        curr_sum += arr[j]
        print(f"i ={i} j= {j} arr ={arr[i:j+1]} , sum= {curr_sum}")
        if curr_sum > s:
            if j - i < min_size:
                min_size = j - i
                min_start = i
            curr_sum -= arr[i]
            i += 1
        else:
            j += 1
    print(arr[min_start: min_start + min_size + 1])
    return arr[min_start: min_start + min_size + 1]
    
    
    
    
    
    
assert [4, 45, 6] == smallest_sub_arr_v2([1, 4, 45, 6, 0, 19], 51)


