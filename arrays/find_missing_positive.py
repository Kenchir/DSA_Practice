'''
https://leetcode.com/problems/first-missing-positive
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1

'''

'''
TC = O(n)
SC = O(1)
'''
def findMissingPositive(nums):
    
    i, n = 0, len(nums)

    if n == 0:
        return 1
    '''
        Place elements from 1 to n to the correct places
    '''
    while i < n:

        if nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1

    for i in range(n):
        
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1

k= [ -1, -10,5,1,3,0,4,2,-2,0,0] #[7,8,9,11,12]

print(findMissingPositive(k))