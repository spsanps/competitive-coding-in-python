def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    from bisect import bisect_left
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return pos if pos != hi and a[pos] == x else -1  # don't walk off the end


def binary_search_presence(l, x):
    from bisect import bisect_left
    pos = bisect_left(l, x)
    if pos == len(l):
        return False
    elif l[pos] != x:
        return False
    else:
        return True


def bs_func_int(f, y):
    lb = 0
    ub = 1

    while f(ub) < y: ub <<= 1

    while lb != ub:
        mid = (lb + ub) / 2

        if f(mid) > y: ub = mid
        elif f(mid) < y: lb = mid
        else: break

        #print lb, ub

    else: return -1

    return mid


if __name__ == '__main__':
    #print bs_func_int(lambda x: x*x, 78)
    print binary_search_presence([1, 2, 5, 7, 9], 5)
    print binary_search_presence([1, 2, 5, 7, 9], 1)
    print binary_search_presence([1, 2, 5, 7, 9], 9)
    print binary_search_presence([1, 2, 5, 7, 9], 0)
    print binary_search_presence([1, 2, 5, 7, 9], 10)
    print binary_search_presence([1, 2, 5, 7, 9], 6)
