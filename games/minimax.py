def evaluate(gs):
    raise NotImplementedError


def mini_max(game_state):
    return max(map(lambda move: (move, min_play(game_state.next_state(move))),
                   game_state.get_available_moves()),
               key=lambda x: x[1])


def min_play(game_state):
    if game_state.is_game_over():
        return evaluate(game_state)
    return min(map(lambda move: max_play(game_state.next_state(move)),
                   game_state.get_available_moves()))


def max_play(game_state):
    if game_state.is_game_over():
        return evaluate(game_state)
    return max(map(lambda move: min_play(game_state.next_state(move)),
                   game_state.get_available_moves()))
