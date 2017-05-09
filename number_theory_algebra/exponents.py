'''mod = 10 ** 9 + 7

for _ in range(input()):
    a, b = [int(x) for x in raw_input().split()]
    b %= mod - 1
    print pow(a, b, mod)

for _ in range(input()):
    a, b = [int(x) for x in raw_input().split()]
    print pow(a, b, 10 ** 9 + 7)
'''

from matrices import Mat


def fast_exp(a, b):
    if b == 0: return 1
    if b == 1: return a
    if b % 2 == 0:
        return fast_exp(a, b / 2) ** 2
    else:
        return a * (fast_exp(a, (b - 1) / 2) ** 2)


if __name__ == '__main__':
    print fast_exp(Mat([[1, 1], [1, 0]]), 103)

