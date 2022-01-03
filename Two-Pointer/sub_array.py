'''
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:
 min_sub_array_length([2,3,1,2,4,3], 7) returns 2

 Explanation: the subarray [4,3] has the minimal length under the problem constraint.

[2,3,1,2,4,3]

[0,1,2,3,4,5]


'''

# Brute force
'''
    O(n^2) Worst Time  complexity and O(1) best Time complexity

    O(1) space compexity : no extra data structure used
'''

from typing import SupportsComplex


def min_sub_array(arr,sum):

    if len(arr) == 1:
        if arr[0] == sum:
            return 1
        return 0

    minLength=float('inf')

    for index in range(0,len(arr)):
        if arr[index] == sum:
            return 1

        elif arr[index] > sum:
            minLength = 1

        else:
            # print(arr[index])
            new_sum = arr[index]
            for pointer in range(index+1,len(arr)):
                new_sum +=  arr[pointer]

                if new_sum >= sum:
                    temp_len = pointer - index + 1

                    minLength = temp_len if temp_len < minLength else minLength
                 
                    break

    return minLength  if minLength != float('inf') else 0              


        
print(min_sub_array([2,3,1,2,4,3], 5))

'''
Two pointer
'''
def min_array_2(arr,sum):

    if len(arr)<1:
        return 0
    if len(arr) == 1:
        return 1 if arr[0] >=  sum else 0
    
    i,j, n = 0,0,len(arr)

    temp_sum = 0
    min_length= float('inf')

    while i < n and j < n:
        if arr[j] == sum:
            return 1
        
        if temp_sum >= sum:
            print(" i: ",i, " j: ",j)
            temp_len = j - i +1
            min_length = min(min_length, temp_len)
            temp_sum -= arr[i]
            i += 1

        else:
            temp_sum += arr[j]
            if temp_sum < sum:
                j += 1
    
    return min_length if min_length != float('inf') else 0


print(min_array_2([2,3,1,2,4,3], 7))





    

