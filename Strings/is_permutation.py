"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.

Solns:
1.
 Check if length is same , if not return False
 Sort the strings  and compare if equal
"""
from functools import cache
from math import inf


def is_permutation_1(s1, s2):
    if len(s1) != len(s2):
        return False
    
    return "".join(sorted(s1)) == "".join(sorted(s2))


test1_s1, test1_s2 = "dog is not cat", "is cat not dog"
test2_s1, test2_s2 = "jane is doe ", "doe jane"
assert True == is_permutation_1(test1_s1, test1_s2)
assert False ==  is_permutation_1(test2_s1, test2_s2)

"""
Solns 2: assuming we are using ASCII characters : max should be 128.
Use count of chars to find duplicates
"""

def is_permutation_2(s1, s2):
    if len(s1) != len(s2):
        return False
    chars = [0] * 128
    
    for char in s1:
        chars[ord(char)] += 1
    
    for char in s2:
        chars[ord(char)] -= 1
        if chars[ord(char)] == -1:
            return False
    return  True

assert True == is_permutation_2(test1_s1, test1_s2)
assert False ==  is_permutation_2(test2_s1, test2_s2)
    
    
    
class Solution:
    def maxSubArray(self, nums):
        @cache
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else -inf
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)