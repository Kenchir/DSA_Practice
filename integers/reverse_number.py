'''
Given integer N, return the reverse of it.

e.g : 123 -> 321
    100 -> 1


'''

def reverseNumber(N):
    if N > -10 and N < 10:
        return N
    
    sign, N = -1 if N < 0 else 1, abs(N)
    reversedN = N % 10
    N = N // 10

    while N != 0:
        
        reversedN = reversedN * 10 + N % 10
        N = N // 10
    
    return reversedN * sign


print(reverseNumber(123))
print(reverseNumber(-123))
print(reverseNumber(100))
print(reverseNumber(9))


