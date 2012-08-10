from .objects import ObjectGenerator


class ObjectListGenerator(object):

    def __init__(self, cls, min=0, max=1):
        self.cls = cls
        self.min = abs(min)
        self.max = max(min, abs(max))

    def actions(self):
        pass
