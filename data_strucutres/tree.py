reps = []


class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, obj):
        self.children.append(obj)

    def df_count(self):
        total = len(self.children)
        for c in self.children:
            total += c.dfs_count()

    def dfs(self, val):
        for c in self.children:
            if c.data == val:
                return c
            else:
                c = c.dfs(val)
                if c != -1:
                    return c
        return -1

    def find_rep(self):
        if self.parent is None:
            return self
        else:
            return self.parent.find_rep()
