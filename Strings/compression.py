"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints:#92, #110
aabcccccaaa

ab
"""


def compress_string(s):
    n = len(s)
    if n == 1:
        return -1
    arr = [None] * n
    index = 0
    i, j, count = 0, 1, 1
    while j < n:
        if s[i] == s[j]:
            count += 1
            j += 1
            arr[index] = f"{s[i]}{count}"
        else:
            arr[index] = f"{s[i]}{count}"
            i, count, j, index = j, 1, j + 1, index + 1
            arr[index] = f"{s[i]}{count}"
    
    st  = "".join(arr[:index +1])
    if len(st) > n:
        return  - 1
   
    return st

assert -1 == compress_string("abc")
assert "a2b1c5a3"== compress_string("aabcccccaaa")