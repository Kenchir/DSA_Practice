'''
Given number n, return its fibonacci'''

'''
Time complexity : O(n)
Space complexity : O(n)

The space needed is for the stack trace where recursive function is called
'''
k = 5

m = 0


def fib(n):
    global m
    m = m + 1
    if n == 1:
        return 1
    
    if n == 0:
        return 0
    
    return fib(n - 1) + fib(n - 2)


print(fib(12))

'''
Time complexity : O(2^n)
Space complexity : O(n) - stack trace

'''


def fib_dynamic_programming(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for i in range(1, n):
        prev, curr = curr, curr + prev

    return curr


"""
TC = O(n)
SC = O(1)
"""

print(fib_dynamic_programming(12))
