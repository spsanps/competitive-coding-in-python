def mex(s):
    l = sorted(s)
    i = 0
    while l and (i == l.pop(0)):
        i += 1
    return i


def create_grundy(game_state, n):
    g = [None for _ in xrange(n)]

    def grundy(gs):
        if g[gs.data] is not None: return g[gs.data]

        if gs.is_game_over():
            g[gs.data] = 0
            return 0
        else:
            lower_states = [gs.next_state(move) for move in gs.get_available_moves()]
            gru = mex([grundy(ls) for ls in lower_states])
            g[gs.data] = gru

    grundy(game_state)

    return g
