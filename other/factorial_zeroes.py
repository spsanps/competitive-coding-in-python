"""Problem Statement

Manasa was sulking her way through a boring class when suddenly her teacher singled her out and asked her a question.
He gave her a number n and Manasa has to come up with the smallest number m which contains atleast n number of zeros at the end of m!.
Help Manasa come out of the sticky situation.

Input Format
The first line contains an integer T i.e. the number of Test cases.
Next T lines will contain an integer n.

Output Format
Print smallest such number m."""


def fun(x):
    if x < 5:
        return 0
    return (x / 5) + fun(x / 5)


for i in xrange(int(input())):
    m = int(input())
    begin = 0
    end = m * 5
    temp = 0
    while end - begin > 1:
        mid = (begin + end) >> 1
        if fun(mid) < m:
            begin = mid
        else:
            end = mid
    print end
