def subArraySum(arr, n, s):
     
        i, j = 0, 1
        curr_sum = arr[i]
        found = False
        if curr_sum == s:
            found = True
        while j < n :
            print(f"curr_sum={curr_sum} i={i} j={j}")
            if found:
                if curr_sum + arr[j] > s:
                    return [i + 1, j]
              
                j += 1
            else:
                if curr_sum + arr[j] == s:
                    curr_sum = s
                    found = True
                    j += 1
                elif curr_sum + arr[j] > s:
                    if s == curr_sum - arr[i] + arr[j]:
                        curr_sum = s
                        found = True
                        i += 1
                        j += 1
                    else:
                        i += 1
                else:
                    curr_sum = curr_sum + arr[j]
                    j += 1
        if curr_sum == s:
            if i + 1 == j:
                return [i + 1]
            return [i + 1, j]
        return [-1]


# print(subArraySum([4, 1, 2, 3, 7, 5], 6, 13)) 1 0
# 0
print(subArraySum([0], 1, 0))