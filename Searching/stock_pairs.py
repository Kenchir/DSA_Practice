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