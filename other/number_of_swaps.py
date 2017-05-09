def number_of_swaps(l1, l2):
    """
    Doesn't work with if elements are repeated
    :param l1:
    :param l2:
    :return:
    """
    permutation = map(l1.index, l2)
    # print permutation
    n_swaps = 0
    seen = set()
    for i in xrange(len(permutation)):
        if i not in seen:
            j = i
            while permutation[j] != i:
                j = permutation[j]
                seen.add(j)
                n_swaps += 1
    return n_swaps


if __name__ == "__main__":
    n = 5
    L1, L2 = range(n), range(n)
    from random import shuffle

    shuffle(L2)
    print L1, L2
    print "Number of swaps:", number_of_swaps(L1, L2)
