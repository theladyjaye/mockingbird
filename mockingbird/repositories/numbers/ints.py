from itertools import repeat
from random import randrange
from mockingbird.utils import safe_range
from mockingbird.compat import map


class IntGenerator(object):

    def __init__(self, min=1, max=1, value=None):

        if value:
            self.generator = repeat(value)
        else:
            min, max = safe_range(min, max)
            self.generator = map(randrange, repeat(min), repeat(max))

    def action(self, context):
        return next(self.generator)
