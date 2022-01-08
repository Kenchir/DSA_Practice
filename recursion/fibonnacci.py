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
  if n == 1 :
    return 1

  if n == 0:
    return 0


  return fib(n - 1) + fib(n - 2)

print(fib(k))


'''
Time complexity : O(n)
Space complexity : O(1)

'''
def fib_iterative(n):

  i, n1, n2 =0, 0, 1

  while i < n:
    n1, n2 = n2, n1 + n2
    i += 1

  return n2 
   



print(fib_iterative(k))
