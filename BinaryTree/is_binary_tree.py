'''
    Given integer N and K,  return a palindrome string of length N and K distinct lowercase letters. 
    i.e letters (a -z)
    Example:  
        N = 3, K = 2 ->  aba, opo,yzy ... etc
        N = 5, K = 3 ->  hhkhh, mnpnm

TC = O(N)
SC = O(N)
'''

def sol(N,K):
    letters = "abcdefghijklmnopqrstuvwxyz"

    result=""
    

    if  N - K == 1:
        result += letters[:K]
        result += result[0]

    else:
        result = letters[:K]
        last, N = result[-1],N - K
   
        for i in range(N-K):
            result += last
        

        if N+K %2 !=0:
            result += last

        result += result[:K-1][::-1]

    return result

print(sol(11,7))