'''
Find number of pairs (x,y) in an array such that x ^ y > y ^x

input : X= [2,1,6], Y= [1,5]

Output = 3

'''

'''
Brute force solution

TC = O(len(X) *len(Y))
'''
def pairs(X,Y):
    # X.sort()
    # Y.sort()

    pairs = 0

    for x in X:
        for y in Y:
            if x ** y > y ** x:
                pairs += 1
    return pairs

# print(pairs( [2,1,6],[1,5]))
# print(pairs([10, 19, 18],[11, 15, 9]))

'''
Improvement 
TC = O(len(Y) * log(len(X)))
   = O(nlogn)
'''
def pairs2(X,Y):

        # return 0
    
    X.sort()


    pairs =0

    for y in Y:
        # print(search(y))
        pairs += search(y)
      
    return pairs
    
def search(num, X):
        # print(y)
        if X[0] >= num:
            return 0
        # print(X)
        if X[-1] < num:
            return len(X)

        start, end  = 0, len(X)-1

        while start <= end:
            mid = start + (end - start)//2
        
            if X[mid] >= num and X[mid -1]  < num:
               return   mid 

            elif X[mid] <= num and X[mid + 1] > num:
                return mid + 2
                
            else:
                start = mid + 1
print(pairs2( [2,1,6],[1,5]))
print(pairs2( [2,1,6],[1,2,2,2]))


# print(pairs2([10, 19, 18],[11, 15, 9]))