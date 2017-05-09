# coding=utf-8
"""The factorial length of a number is defined here as the sum of prime powers in the number's factorization; for example:
factorialLength(6)=2. 6=2^1×3^1. Summing the powers, we get 1+1=2.
factorialLength(12)=3. 12=2^2×3^1. Summing the powers, we get 2+1=3.

Given an array, A, of N integers (where A={a0,a1,…,an−2,aN−1}), we define a super-subsequence (S) of a subsequence (A′) to be the sequence of factorials of each number in A′. For instance, if A′={aj+0,aj+1,…,aj+k−1} denotes a subsequence of length k (where j is the jth index of A and 0≤j+k≤N−1), then the corresponding super-subsequence would be S={(aj+0)!,(aj+1)!,…,(aj+k−1)!}. Recall that ! denotes Factorial.

The pleasing value of a super-subsequence (S) is defined here as the sum of the factorial lengths of all the numbers in S.

Find and print the sum of factorial lengths for all super-subsequences with an even pleasing value."""
import math


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


def number_line():
    inp = raw_input()
    return map(int, inp.split())


n = input()
l = number_line()
M = max(l)
primes = rwh_primes3(M + 1)


def timesinf(n, p):
    c = 0
    while n >= p:
        N = int(math.log(n, p))
        c += (p ** N - 1) / (p - 1)
        n -= p ** N
    return c


def fact_len(n):
    c = 0
    for p in primes:
        if p > n: break
        c += timesinf(n, p)
    return c


l = map(fact_len, l)

for i in xrange(n):
    for j in xrange(i + 1, n + 1):
        c_l = l[i:j]
        if len(c_l) == 0: continue
        if sum(c_l) % 2 == 0: print sum(c_l)
