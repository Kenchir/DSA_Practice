'''
Given number n, return its fibonacci'''

'''
Time complexity : O(n)
Space complexity : O(n)
'''
def fib(n : int) -> int:

  if n == 1 :
    return 1
  if n == 0:
    return 0
  
  return fib(n-1) + fib(n-2)

print(fib(10))