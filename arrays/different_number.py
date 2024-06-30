"""
Getting a Different Number

Given an array arr of unique nonnegative integers, implement a function
getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.

Even if your programming language of choice doesn't have that restriction (like Python),
assume that the maximum value an integer can have is MAX_INT = 2^31-1. So, for instance,
the operation MAX_INT + 1 would be undefined in our case.

Your algorithm should be efficient, both from a time and a space complexity perspectives.
Solve first for the case when you're NOT allowed to modify the input arr.
If successful and still have time, see if you can come up with an algorithm with an improved
space complexity when modifying arr is allowed. Do so without trading off the time complexity.

Analyze the time and space complexities of your algorithm.

Examples:
1. [0, 1, 2, 3] -> 4
2. [1000] -> 0
3. [0, 1, 3, 4] -> 2

"""
def get_different_number(arr):
    """
    TC = O(n)
    SC = O(n)
    :param arr:
    :return:
    """
    size = len(arr)
    arr = set(arr)
    for i in range(size):
        if i not in arr:
            return i
    return size



assert 4 == get_different_number([0, 1, 2, 3])
assert 0 == get_different_number([1000])
assert 2 == get_different_number([0, 1, 3, 4])
