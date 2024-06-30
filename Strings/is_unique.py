"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Soln
each character has an order from 0 to 127.
Use an array of 127
Iterate the string
"""

def is_string_unique(s):
    """Assuming string is ASCII - 128 character length"""
    if len(s) > 128:
        return  False
    """Assuming string only contains a to z  in lower case
    if len(s) > 26:
        return  False
    """
    chars = [False] * 128
    
    for char in s:
        pos = ord(char)
        
        if chars[pos]:
            return False
        chars[pos] = True
    
    return  True
    
    
assert True == is_string_unique("abcd(")
assert False == is_string_unique("hjhkjewo")
assert False == is_string_unique("1hgdd4.")
