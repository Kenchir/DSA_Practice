'''
Given an integer N, return smallest number with same number of digits

eg 1893 should return 10000
'''

def smallestNumber(N):
    if N  < 10 and N >= 0:
        return 0

    smallN = 1

    while N > 10:
        smallN *= 10
        N = N // 10

    return smallN

print(smallestNumber(88946412101545015456))