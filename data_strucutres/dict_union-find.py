"""Instead of the representing referring to itself it refers
to list of one element containing number of elements in that set."""

union_find = {}


def make(obj):
    union_find[obj] = [1]


def find(obj):
    p = union_find[obj]
    if type(p) is list:
        return obj
    else:
        rep = find(p)
        union_find[obj] = rep  # Path compression
        return rep


def union(obj1, obj2):
    r1 = find(obj1)  # representative
    r2 = find(obj2)

    if r1 != r2:
        union_find[r1] = [union_find[r1][0] + union_find[r2][0]]
        union_find[r2] = r1
