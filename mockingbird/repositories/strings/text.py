import pkg_resources
from random import randrange
from itertools import repeat
from itertools import imap
from mockingbird.utils import safe_range


class TextGenerator(object):
    _text = None

    def __init__(self, min=1, max=1, count=None):
        
        if count:
            self.count = repeat(count)
        else:
            min, max = safe_range(min, max)
            self.count = imap(randrange, repeat(min), repeat(max))

    @property
    def text(self):
        if not TextGenerator._text:
            data = pkg_resources.resource_stream("mockingbird.resources",
                                                 "ipsum.txt")
            TextGenerator._text = []

            for line in data:
                TextGenerator._text.append(line.strip())

        return TextGenerator._text

    def words(self):
        # start with a random line from self.text
        index = randrange(0, len(self.text))
        num_words = next(self.count)
        
        data = TextGenerator._text[index].split(" ")

        while len(data) < num_words:
            index = index + 1
            try:
                more = TextGenerator._text[index].split(" ")
                data.extend(more)
            except KeyError:
                more = TextGenerator._text[index].split(" ")
                data.extend(more)

        return ' '.join(data[0:num_words])

    def action(self, context):
        return self.words()

