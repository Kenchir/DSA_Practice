'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
'''
'''
solution implemented using Binary search
'''

'''
 Time = O(log(n))
 Space =O(1)
'''
def mySqrt(num: int) -> int:
    if num <= 1:
        return num

    start=0
    end=num

    while start < end:

        mid=start+(end-start)//2

        square=mid * mid

        if square == num:
            return mid

        elif square < num:
            start=mid+1

        else:
            end=mid
            
    return start-1

assert 2==mySqrt(8)
assert 8==mySqrt(64)
assert 9==mySqrt(99)

def solution(A,B):
    A=list(set(A) & set(B))
    
    
    if len(A) >0:
        min=A[0]
        for index in range(1,len(A)):
            if A[index+1] < min:

                min=A[index+1]
                return min
    return -1
    
    n = min(len(A),len(B))
    for index in range(len(n)):
        if A[index] in  B[index:]:

            return A[index]

    return -1
