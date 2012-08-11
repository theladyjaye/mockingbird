import pkg_resources
from random import randrange
from .names import NameGenerator


class EmailGenerator(object):
    _tlds = None
    _words = None

    @property
    def words(self):
        if not EmailGenerator._words:
            EmailGenerator._words = []

            with pkg_resources.resource_stream("mockingbird.resources",
                                                 "words.txt") as data:
                for line in data:
                    EmailGenerator._words.append(line.strip())

        return EmailGenerator._words

    @property
    def tlds(self):
        if not EmailGenerator._tlds:
            EmailGenerator._tlds = []

            with pkg_resources.resource_stream("mockingbird.resources",
                                                 "tlds.txt") as data:
                for line in data:
                    EmailGenerator._tlds.append(line.strip())

        return EmailGenerator._tlds

    def action(self, context):
        names = NameGenerator()
        first, last = names.action(context).split()

        words = self.words
        tlds = self.tlds

        word_index = randrange(0, len(words))
        tlds_index = randrange(0, len(tlds))

        return "%s@%s.%s" % (first.lower(), words[word_index], tlds[tlds_index])
