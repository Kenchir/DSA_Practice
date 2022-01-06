'''

An array consisting of N intgers is given. We are looking for pairs of elements of the array that are equal but occupy diff positions in the array.
a pair of indices (P,Q) is called identical if  0 <= P < Q < N and A[P] = A[Q]
The goal is to calculate the number of identical pairs of indices.

'''

'''
 Time complexity = O(n^2)
 Space complexity = O(1)

'''
def solutionB(A):
    pairs, start, n = 0, 0, len(A)
    
    while start < n:
        i = start + 1

        while i < n:
            if A[i] == A[start]:
                pairs += 1
            i += 1
        start += 1

    return pairs


'''
 Time complexity = O(n)
 Space complexity = O(n)

'''
def solution(A):
    pairs,  n = 0, len(A)

    if n <= 1:
        return 0

    if n == 2:
        return 1 if A[0] == A[1] else 0
    
    d = {}
    
    for item in A:
        if item in d:
            d[item] += 1

        else:
            d[item] = 1
    
    for val in d.values():
        if val > 1:
            pairs += int(val * (val - 1) * 0.5) 
            '''
                Combination of 2 items without repetition. i.e 
                using n! / k!(n-k)!
                since k = 2
                n! / 2! * n-2!
                hence n * (n -1) /2

            '''
    return pairs if pairs < 1000000000 else 1000000000



print(solution([3,6,5,3,3,5]))


    