
"""
Given a string s, find the length of the longest
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


"""
TC = O(n)
SC = O(n)
"""


def length_of_longest_substring(s: str) -> int:
    
    uniqs = set()
    l, r = 0, 0

    n = len(s)
    max_size = float('-inf')

    while l < n and r < n:
        if s[r] not in uniqs:
            uniqs.add(s[r])
            max_size = max(r - l + 1, max_size)
            r += 1
        else:
            uniqs.remove(s[l])
            l += 1

    return max_size

print(length_of_longest_substring('abcabcbb'))
assert 3 == length_of_longest_substring('abcabcbb')
