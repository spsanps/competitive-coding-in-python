def iter_inp():
    yield input()


def input_numbers():
    import sys
    inp = sys.stdin.read().strip()
    inp = [line.split(' ') for line in inp.split('\n')]
    return [map(int, line) for line in inp]


def input_text():
    import sys
    inp = sys.stdin.read().strip()
    inp = [line.split(' ') for line in inp.split('\n')]
    return inp


def number_line():
    inp = raw_input()
    return map(int, inp.split())


def text_line():
    return raw_input().split()
