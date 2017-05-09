def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


def memo_dict(f):
    """ Memoization decorator for a function taking a single argument
    :param f: func
    """

    class MemoDict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return MemoDict().__getitem__


def mapped_memo_dict(g):
    def decorator(f):
        """ Memoization decorator for a function taking a single argument
        :param f: func
        """

        class MemoDict(dict):
            def __missing__(self, key):
                ret = self[key] = f(self.actual_key)
                return ret

            def __getitem__(self, key):
                self.actual_key = key
                return dict.__getitem__(self, g(key))

        return MemoDict().__getitem__

    return decorator


def mapped_memo(g):
    def mem(f):
        memo = {}

        def helper(x):
            if g(x) not in memo:
                memo[g(x)] = f(x)
            return memo[x]

        return helper

    return mem
