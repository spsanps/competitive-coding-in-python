from math import *
from operator import mul


def number_weights(n):
    """
        Number of distinct number required to represent all values up to n by addition and subtraction
        :param n: Value
        :return: n(distinct numbers)
        """
    if n == 0:
        return 0
    elif n == 2:
        return 2
    return ceil(log(n + 1, 3))


def number_weights_side(n):
    """
    Number of distinct number required to represent all values up to n by addition
    :param n: Value
    :return: n(distinct numbers)
    """
    if n == 0: return 0
    # elif n == 2: return 2
    return ceil(log(n + 1, 2))


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


def e_gcd(a, b):
    """
    Euclid's GCD algorithm implementation
    :param a: Value 1
    :param b: Value 2
    :return: GCD
    """
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


# Recursive algorithm[edit]

def e_gcd_r(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = e_gcd_r(b % a, a)
        # print y, x
        return g, x - (b // a) * y, y


def inverse_mod(a, m):
    g, x, _ = e_gcd(a, m)
    assert g == 1
    return x % m


def chinese_rt(a, n):  # list containing a(s) and n(s) such that x = ai (mod ni)
    N = reduce(mul, n)
    x = 0
    for c in xrange(0, len(n)):
        i = n[c]
        g, r, s = e_gcd(i, N / i)
        assert g == 1
        e = N / i * s
        e %= N
        x += a[c] * e
        x %= N
    return x


# for i in xrange(1025):
#    print i, number_weights_side(i)

if __name__ == '__main__':
    print chinese_rt([2, 3, 1], [3, 4, 5])
    print chinese_rt([2], [3])
    print inverse_mod(2, 10 ** 9 + 7)
    print e_gcd_r(240, 46)
    print gcd(12, 2)
