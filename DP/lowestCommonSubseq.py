"""n, m = map(int, raw_input().strip().split())

D = [['' for j in xrange(m + 1)] for i in xrange(n + 1)]

x = raw_input().strip().split()
y = raw_input().strip().split()

for i in xrange(1, n + 1):
    for j in xrange(1, m + 1):

        if x[i - 1] == y[j - 1]:

            D[i][j] = D[i - 1][j - 1] + x[i - 1] + ' '
        else:
            if len(D[i][j - 1]) > len(D[i - 1][j]):
                D[i][j] = D[i][j - 1]
            else:
                D[i][j] = D[i - 1][j]

print D[-1][-1].strip()
"""


def lcs(x, y):
    n = len(x)
    m = len(y)

    D = [['' for j in xrange(m + 1)] for i in xrange(n + 1)]

    for i in xrange(1, n + 1):

        for j in xrange(1, m + 1):

            if x[i - 1] == y[j - 1]:
                D[i][j] = D[i - 1][j - 1] + x[i - 1] + ' '
            else:
                if len(D[i][j - 1]) > len(D[i - 1][j]):
                    D[i][j] = D[i][j - 1]
                else:
                    D[i][j] = D[i - 1][j]

    return D[-1][-1].strip()


def lcs_len(x, y):
    n = len(x)
    m = len(y)

    dp = [[0 for _ in xrange(m + 1)] for _ in xrange(n + 1)]

    for i in xrange(1, n + 1):

        for j in xrange(1, m + 1):

            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                if dp[i][j - 1] > dp[i - 1][j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]


if __name__ == '__main__':
    print lcs('abcd', 'ad')
    print lcs_len('abcd', 'ad')
