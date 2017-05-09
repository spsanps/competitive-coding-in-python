def primes_sieve2(limit):
    """primality list from [0, limit)"""
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            for n in xrange(i * i, limit, i):  # Mark factors non-prime
                a[n] = False

    return a


def rwh_primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n % 6 > 1)
    n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
    sieve = [True] * (n / 3)
    sieve[0] = False
    for i in xrange(int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) / 3)::2 * k] = [False] * ((n / 6 - (k * k) / 6 - 1) / k + 1)
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) / 3::2 * k] = [False] * (
                (n / 6 - (k * k + 4 * k - 2 * k * (i & 1)) / 6 - 1) / k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in xrange(1, n / 3 - correction) if sieve[i]]


def rwh_primes3(n):
    if n < 6:
        if n <= 2:
            return []
        elif n == 3:
            return [2]
        elif n <= 5:
            return [2, 3]

    correction = (n % 6 > 1)
    n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
    sieve = [True] * (n / 3)
    sieve[0] = False
    for i in xrange(int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) / 3)::2 * k] = [False] * ((n / 6 - (k * k) / 6 - 1) / k + 1)
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) / 3::2 * k] = [False] * (
                (n / 6 - (k * k + 4 * k - 2 * k * (i & 1)) / 6 - 1) / k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in xrange(1, n / 3 - correction) if sieve[i]]


def primeFacs(n):
    primes = rwh_primes2((n / 2) + 1)
    return [x for x in primes if n % x == 0]


def no_prmeFacs(n):
    # Not distinct
    c = 0
    pfs = primeFacs(n)
    for p in pfs:
        while n % p == 0:
            c += 1
            n /= p
    return c


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        #print '\t', f
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


if __name__ == '__main__':
    print primeFacs(100)
    print no_prmeFacs(2)
    print primes_sieve2(6)
