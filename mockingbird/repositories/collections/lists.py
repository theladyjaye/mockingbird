from itertools import islice
from itertools import repeat
from random import randrange
from mockingbird.utils import safe_range
from mockingbird.compat import map


class ObjectListGenerator(object):

    def __init__(self, cls, min=0, max=1, count=None):

        self.cls = cls.__name__

        if count:
            self.count = repeat(count)
        else:
            min, max = safe_range(min, max)
            self.count = map(randrange, repeat(min), repeat(max))

    def action(self, context):
        pool = map(getattr, repeat(context), repeat(self.cls))
        results = islice(pool, 0, next(self.count))
        return list(map(lambda x: x(), results))
