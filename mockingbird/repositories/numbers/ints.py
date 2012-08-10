from itertools import repeat
from itertools import imap
from random import randrange


class IntGenerator(object):

    def __init__(self, min=1, max=2):
        self.generator = imap(randrange, repeat(min), repeat(max))

    def action(self):
        return next(self.generator)
