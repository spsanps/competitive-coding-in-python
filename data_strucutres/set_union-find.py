class UnF:
    def __init__(self):
        self.union_find = {}

    def make(self, obj):
        self.union_find[obj] = [1]

    def find(self, obj):
        p = self.union_find[obj]
        if type(p) is list:
            return obj
        else:
            rep = self.find(p)
            self.union_find[obj] = rep  # Path compression
            return rep

    def union(self, obj1, obj2):
        r1 = self.find(obj1)  # representative
        r2 = self.find(obj2)

        if r1 != r2:
            self.union_find[r1] = [self.union_find[r1][0] + self.union_find[r2][0]]
            self.union_find[r2] = r1
