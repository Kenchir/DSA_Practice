'''

https://leetcode.com/problems/maximum-erasure-value

You are given an array of positive integers nums and want to erase a subarray containing unique elements.
 The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 
Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
'''

'''
Time = O(n)
Space = O(n)
'''
def max_erase(nums):

    my_set = set()

    max_sum,ans,i,j ,n= 0,0,0,0,len(nums)

    while i <  n and j < n:

        if nums[j] not in my_set:
            
            max_sum += nums[j]
            ans = max(ans,max_sum)
            my_set.add(nums[j])
            j +=1
        
        else:

            max_sum -= nums[i]
            my_set.remove(nums[i])
            i += 1
    
    return ans


print(max_erase([4,2,4,5,6]))