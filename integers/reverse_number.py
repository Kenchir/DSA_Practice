"""
Given integer N, return the reverse of it.

e.g : 123 -> 321
    100 -> 1


"""


def reverse_number(n):
    if -10 < n < 10:
        return n
    
    sign, n = -1 if n < 0 else 1, abs(n)
    reversed_n = n % 10
    n = n // 10

    while n != 0:
        reversed_n = reversed_n * 10 + n % 10
        n = n // 10
    
    return reversed_n * sign


print(reverse_number(123))
print(reverse_number(-123))
print(reverse_number(100))
print(reverse_number(9))
print(re)

