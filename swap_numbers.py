"""
Number Swapper: Write a function to swap a number in place (that is, without temporary variables).

i.e a = 10, b = 20
use difference
a = b - a  ->  10
b =  b - a
a = a + b

"""


def swap_numbers(a, b):
    a = b - a
    b = b - a
    a = a + b
    
    return a, b


assert (2, 4) == swap_numbers(4, 2)
assert (53, 12) == swap_numbers(12, 53)
assert (12, -20) == swap_numbers(-20, 12)


