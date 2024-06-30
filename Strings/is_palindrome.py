

''''
TC = O(n/2)
SC = O(1)
'''

def is_palindrome(s):

    start, end = 0, len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

assert True == is_palindrome("abba")
assert False == is_palindrome("abracadabra")
