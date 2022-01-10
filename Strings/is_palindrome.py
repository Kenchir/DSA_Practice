

''''
TC = O(n/2)
SC = O(1)
'''

def isPalindrome(s):

    start, end = 0, len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

print(isPalindrome("abba"))