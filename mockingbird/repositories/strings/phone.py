from itertools import repeat
from itertools import islice
from random import randrange
from mockingbird.compat import map


class PhoneNumberGenerator(object):

    def action(self, context):
        number = "%i" % randrange(2, 10)
        numbers = map(randrange, repeat(0), repeat(10))
        number = number + "%i%i-%i%i%i-%i%i%i%i"
        return number % tuple(islice(numbers, 0, 9))
