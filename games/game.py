class GameState:
    def __init__(self, start=None):
        self.data = start

    def next_state(self, move):
        raise NotImplementedError

    def is_game_over(self):
        raise NotImplementedError

    def get_available_moves(self):
        raise NotImplementedError


def evaluate(gs):
    raise NotImplementedError
