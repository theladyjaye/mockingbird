from itertools import repeat
from itertools import imap
from random import randrange

class ChoiceGenerator(object):

    def __init__(self, choices):
        self.range = imap(randrange, repeat(0), repeat(len(choices)))
        self.choices = choices

    def action(self):
        return self.choices[next(self.range)]

class BooleanGenerator(ChoiceGenerator):

    def __init__(self, value=None):

        if type(value) is bool:
            self.choices = [value]
        else:
            self.choices = [True, False] 
        
        self.range = imap(randrange, repeat(0), repeat(len(self.choices)))