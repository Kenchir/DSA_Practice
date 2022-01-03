
'''
 Given two arrays, return the minimum number that is on both arrays. 

 If no minimum number exists on both, return -1

'''

def solution(A,B):
    if len(A) ==0 or len(B) == 0:

        return -1

    A=list(set(A) & set(B))
    

    if len(A) > 0:
        print(A)
        min = A[0]
        for index in range(1,len(A)):

            if A[index] < min:
                min = A[index]  
                return min

    return -1

print(solution([],[21,8,7,4,2,1]))