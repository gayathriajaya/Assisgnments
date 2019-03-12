#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import product


def is_palindrome(n):
    s=str(n)
    return  s==s[::-1]



max_pro =max(x*y for x,y in product(range(1000),repeat=2) if is_palindrome(x*y))
print(max_pro)
