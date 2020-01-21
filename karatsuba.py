import math

def num_digits(num: int) -> int:
    """
    Return number of digits for a base10 integer
    """
    n = math.ceil(math.log10(num))
    if num%10 == 0:
        n += 1
    return n

def split_num_at(num: int, pos: int) -> (int, int):
    """
    Return parts after splitting an integer into 2 parts
    at index given by pos, starting from right
    """
    prefix = num // (10**pos)
    suffix = num % (10**pos)
    return prefix, suffix

def multiply_karatsuba(num1: int, num2: int) -> int:
    if num1<10 or num2<10:
        return num1*num2

    # find splitting point of smaller number
    n = min(num_digits(num1), num_digits(num2))
    split_at = n - n//2

    # split numbers
    a, b = split_num_at(num1, split_at)
    c, d = split_num_at(num2, split_at)

    # compute sub-products
    ac = multiply_karatsuba(a, c)
    bd = multiply_karatsuba(b, d)
    z = multiply_karatsuba(a + b, c + d)
    # comput ad + bc
    adbc = z - ac -bd

    # join products with exponents
    prod = (10**n) * ac + (10**split_at) * adbc + bd
    return prod
