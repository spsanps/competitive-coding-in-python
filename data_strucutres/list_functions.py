def cumulative(lis):
    total = 0
    for x in lis:
        total += x
        yield total
