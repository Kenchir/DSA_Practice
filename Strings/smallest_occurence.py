'''
Write a function solution that, given a string S of length N, returns the length of the shortest unique substring of S, 
that is, the length of the shortest word which occurs in S exactly once.

Examples:

1. Given S = "abaaba", the function should return 2. The shortest unique substring of S is "aa".

2. Given S = "zyzyzyz", the function should return 5.
 The shortest unique substring of S is "yzyzy". Note that there are shorter words, like "yzy", occurrences of which overlap, but they still count as multiple occurrences.

3. Given S = "aabbbabaaa", the function should return 3. All substrings of size 2 occurs in S at least twice.

Assume that:

N is an integer within the range [1..200];
string S consists only of lowercase letters (a−z).
In your solution, focus on correctness. The performance of your solution will not be the focus of the
'''
'''
Time complexity : O(n ^ 2)
Space complexity : O(n)
'''
def smallestSubstring(S):
    substrings, start, end = [], 0 , len(S) - 1

    while start <= end:
        i = start + 1

        while i <= end:
            substrings.append(S[start:i])
            i +=1
            
        start += 1

    uniques = set(substrings)
   
    length =float('inf')
    for  item in uniques:
        if substrings.count(item) == 1:
            length = min(length,len(item))
            
    return length


print(smallestSubstring("aabbbabaaa"))
