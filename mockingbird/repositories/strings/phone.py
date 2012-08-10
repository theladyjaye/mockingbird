from itertools import repeat
from itertools import imap
from itertools import islice
from random import randrange


class PhoneNumberGenerator(object):

    def action(self, context):
        number = "%i" % randrange(2, 10)
        numbers = imap(randrange, repeat(0), repeat(10))
        number = number + "%i%i-%i%i%i-%i%i%i%i"
        return number % tuple(islice(numbers, 0, 9))
