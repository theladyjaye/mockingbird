from itertools import repeat
from random import randrange
from mockingbird.compat import map


class ChoiceGenerator(object):

    def __init__(self, choices):
        self.range = map(randrange, repeat(0), repeat(len(choices)))
        self.choices = choices

    def action(self, context):
        return self.choices[next(self.range)]


class BooleanGenerator(ChoiceGenerator):

    def __init__(self, value=None):

        if type(value) is bool:
            self.choices = [value]
        else:
            self.choices = [True, False]

        self.range = map(randrange, repeat(0), repeat(len(self.choices)))
