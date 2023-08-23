"""
Reverse a string with recursion

Space complexity = O(n) - extra array used to store reversed string
Time complexity = T(n) -
"""


def reverse_string(s: str, s_arr=None, pos=None) -> str:
    if s_arr is None:
        s_arr = []
    
    if pos is None:
        if len(s) == 0:
            return s
        pos = len(s) - 1
    
    if pos - 1 == -1:
        s_arr.append(s[pos])
        return "".join(s_arr)
    
    s_arr.append(s[pos])
    return reverse_string(s, s_arr, pos - 1)


assert "dcba" == reverse_string("abcd")
assert "" == reverse_string("")
assert "z" == reverse_string("z")
assert "".join(reversed("abracadabra")) == reverse_string("abracadabra")
