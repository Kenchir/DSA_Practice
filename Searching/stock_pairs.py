
'''
Given an integer array of stockprofit and a target int.
Find and  return number  distinct stock pairs whose sum is equal to the target.


'''

def stockpairs(stockprofit, target):

    stockprofit.sort()

    pairs, low, high =[], 0, len(stockprofit)-1
   
    while low < high:
       
        pair_sum = stockprofit[low] + stockprofit[high]
        if pair_sum == target:

            if [stockprofit[low] , stockprofit[high]] not in pairs:
                pairs.append([stockprofit[low] , stockprofit[high]])  
           
            low += 1
        
        elif pair_sum < target:
            low += 1

        else:
            high -= 1

    return len(pairs)

    
print(stockpairs([5,7,9,13,11,6,6,3,3],12))