from functools import cache
from math import inf


def maxSubArray(nums):
    @cache
    def solve(i, must_pick):
        print(i , must_pick)
        if i >= len(nums):
            print(i)
            return 0 if must_pick else -inf
        return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
    return solve(0, False)

# maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = -inf
    current_sum = 0
    for x in numbers:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
        print(f"x = {x}, best_sum = {best_sum}, current_sum={current_sum}")

    return best_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))