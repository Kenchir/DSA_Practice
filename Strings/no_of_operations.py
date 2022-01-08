'''
Given string S of length N which is in binary form corresponding to non negative V integer.
if V is odd, subtract 1 from it, else divide by 2.

Find max operation to to reduce V to 0
'''
'''
TC = O(n) worst case
SC = 0

'''
def maxOperations(S):
    S, operations = int(S,2), 0
    
    while S != 0:
        if S % 2 == 0:
            S = S // 2
        
        else:
            S -= 1
        operations += 1
    
    return operations

print(maxOperations("1" * 400000))