"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
"""

def urlify(s, true_length):
    pass
    # p = list(str)
    # space_count, index, i = 0, 0 ,0
    # for char in s:
    #     if char == ' ':
    #         space_count += 1
    #
    # index = true_length + space_count * 2
    #
    # if len(s)
    #
    # return "".join([c if c!= ' ' else '%20' for c in s])

print(urlify("Mr John Smith "))
assert "Mr%20John%20Smith" == urlify("Mr John Smith ")