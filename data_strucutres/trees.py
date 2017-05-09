class Node:
    def __init__(self, val=None):
        self.value = val
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __repr__(self, tree=True, level=0):
        if not tree: return self.value
        ret = "\t" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def __iter__(self):
        for child in self.children:
            for v in child.__iter__():
                yield v
        yield self

    def all_predecessors(self):
        for child in self.children:
            for c in child.all_predecessors():
                yield c
            yield child


def make_tree(list_value):
    nodes = dict(((val[0], Node(val[0])) for val in list_value))
    start = nodes[list_value[0][0]]

    for parent, child in list_value:

        if child in nodes:
            child_node = nodes[child]
        else:
            child_node = Node(child)

        nodes[parent].add_child(child_node)

        if start is child_node: start = nodes[parent]

    return start


if __name__ == '__main__':
    ls = """5 2
3 2
3 1
1 4
1 5"""

    ls = ls.split('\n')

    ls = [map(int, i.split()) for i in ls]

    t = make_tree(ls[1:])

    c = 0
    T = 2
    for n in t:
        n_val = n.value
        similar = [v for v in n.all_predecessors() if abs(v.value - n_val) <= T]
        c += len(similar)

    print c
