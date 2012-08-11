import pkg_resources
from random import randrange
from itertools import repeat
from mockingbird.utils import safe_range
from mockingbird.compat import map


class TextGenerator(object):
    _text = None

    def __init__(self, min=1, max=1, count=None):

        if count:
            self.count = repeat(count)
        else:
            min, max = safe_range(min, max)
            self.count = map(randrange, repeat(min), repeat(max))

    @property
    def text(self):
        if not TextGenerator._text:
            TextGenerator._text = []

            with pkg_resources.resource_stream("mockingbird.resources",
                                                "ipsum.txt") as data:
                for line in data:
                    line = line.decode('utf8')
                    TextGenerator._text.append(line.strip())

        return TextGenerator._text

    def words(self):
        # start with a random line from self.text
        index = randrange(0, len(self.text))
        num_words = next(self.count)

        data = TextGenerator._text[index].split()

        while len(data) < num_words:
            index = index + 1
            try:
                more = TextGenerator._text[index].split()
                data.extend(more)
            except KeyError:
                more = TextGenerator._text[index].split()
                data.extend(more)

        return ' '.join(data[0:num_words])

    def action(self, context):
        return self.words()

