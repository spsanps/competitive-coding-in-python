def input_numbers():
    import sys
    inp = sys.stdin.read().strip()
    inp = [line.split(' ') for line in inp.split('\n')]
    return [map(int, line) for line in inp]


def input_numbers2(inp):
    inp = [line.split(' ') for line in inp.split('\n')]
    return [map(int, line) for line in inp]


inp = """0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0 0 0
0 0 0 3 2 1 3 0 0 0
0 0 0 0 2 2 0 0 0 0
0 0 0 3 1 1 2 3 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1"""

inp = input_numbers2(inp)

grid = inp[:-1]
for c in  grid:
    print c
player = inp[-1][0]

print player
# del inp


def search(board, pos, ply, direction=(0, 1)):
    r_, c_ = pos
    for i in xrange(2, 11):
        r = r_ + direction[0] * i
        c = c_ + direction[1] * i
        if r > 9 or c > 9 or r < 0 or c < 0: return 0, board
        #print len(board), len(board[0])
        if board[r][c] != 1 or board[r][c] != 2: return 0, board
        if board[r][c] == ply:
            print i - 1
            return i - 1, board
        board[r][c] = ply


def copy_board(board):
    return [list(row) for row in board]


def move_evaluate(board, ply, move):
    n_board = copy_board(board)
    f = lambda d: search(n_board, move, ply, d)
    return sum([f(d)[0] for d in ((0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (-1, 0), (0, -1))]), n_board


def evaluate(board, ply):
    c = 0
    for row in board:
        for elem in row:
            if elem == ply:
                c += 1
    return c


def other_ply(ply):
    return 1 if ply == 2 else 2


def no_depth_pick(board, ply):
    r_boards = {}
    n_board = copy_board(board)
    for r in xrange(0, 10):
        for c in xrange(0, 10):
            v, b = move_evaluate(board, ply, (r, c))
            r_boards[(r, c)] = b
            n_board[r][c] = v * 10

    max_v = 0
    max = (None, None)
    for r in xrange(0, 10):
        for c in xrange(0, 10):
            if n_board[r][c] >= 10 and n_board[r][c] >= max_v:
                max = (r, c)

    if max == (None, None): return board
    return r_boards[max]


def evaluate_moves(board, ply, depth=10):
    for r in xrange(0, 10):
        for c in xrange(0, 10):
            v, b = move_evaluate(board, ply, (r, c))
            if v > 0:
                print v
                ply_c = ply
                for i in xrange(depth):
                    ply_c = other_ply(ply_c)
                    b = no_depth_pick(b, ply_c)
                board[r][c] == evaluate(b, ply) + 10

    #print board

    max_v = 0
    max = (None, None)
    for r in xrange(0, 10):
        for c in xrange(0, 10):
            if board[r][c] >= 10 and board[r][c] >= max_v:
                max = (r, c)

    return max


print evaluate_moves(grid, player)
