import fractions


def reduce_fraction(a, b):
    gcd = fractions.gcd(a, b)
    return a / gcd, b / gcd
