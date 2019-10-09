def can_play(f):
    def wrap(self, *args):
        if self.can_play:
            f(self, *args)
    return wrap
