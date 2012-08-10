from itertools import repeat
from itertools import imap
from random import randrange


class IntGenerator(object):

    def __init__(self, min=1, max=1):
        self.generator = imap(randrange, repeat(min), repeat(max))


    def action(self):
        return next(self.generator)


class BooleanGenerator(IntGenerator):

    def __init__(self, value=None):
        self.min = 0
        self.max = 2
        self.value = value

    def action(self):
        if self.value:
            return self.value
        else:
            return bool(super(BooleanGenerator, self).action())
