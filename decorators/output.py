def print_play(f):
    def wrap(*args):
        result = f(*args)
        print(result)
        return result
    return wrap


def print_board(f):
    def wrap(*args, **kwargs):
        print(f'The board is now:', ' '.join([f'<{tile.side1}:{tile.side2}>' for tile in args[2]]))
        return f(*args, **kwargs)
    return wrap
