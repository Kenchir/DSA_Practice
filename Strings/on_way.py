"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

"""


def is_one_way(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    dict_ = {}
    
    for char in s1:
        if char in dict_:
            dict_[char] += 1
        else:
            dict_[char] = 1
    
    op_done = False
    for char in s2:
        if char in dict_:
            dict_[char] -= 1
            if dict_[char] == -1:
                 if op_done:
                     return False
                 op_done = True
        else:
            if op_done:
                return False
            op_done = True
    return True


for s, expected in zip([["pale", "ple"], ["pales", "pale"], ["pale", "bale"], ["pale", "bake"]],
                       [True, True, True, False]):
    print(s, expected)
    assert expected == is_one_way(s[0], s[1])
    
p:str ="aaa"

"""
bal - > bael

"""

def is_one_way_two(s1, s2):
    def  is_insert_delete(s1, s2):
        index1, index2 = 0, 0
        while index1 < len(s1) and index2 < len(s2):
            if s1[index1] != s2[index2]:
                if index2 != index1:
                    return False
                else:
                    index2 += 1
            else:
                index2 += 1
                index1 += 1
        return True
        
    if len(s1) == len(s2): # replacement
        found = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if found:
                    return False
                found = True
        return True
    
    elif abs(len(s1) - len(s2)) == 1:
        if len(s1) > len(s2):
            return is_insert_delete(s2, s1)
        return is_insert_delete(s1, s2)
    return False
    

for s, expected in zip([["pale", "ple"], ["pales", "pale"], ["pale", "bale"], ["pale", "bake"]],
                       [True, True, True, False]):
    print(s, expected)
    assert expected == is_one_way_two(s[0], s[1])
    
    
    