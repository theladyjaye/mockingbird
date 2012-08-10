import pkg_resources
from random import randrange


class LoremIpsumGenerator(object):
    _text = None

    def __init__(self, min=1, max=1):
        self.min = min
        self.max = max
        self.is_range = True if max - min > 1 else False

    @property
    def text(self):
        if not LoremIpsumGenerator._text:
            data = pkg_resources.resource_stream("mockingbird.resources",
                                                 "ipsum.txt")
            LoremIpsumGenerator._text = []

            for line in data:
                LoremIpsumGenerator._text.append(line.strip())

        return LoremIpsumGenerator._text

    def words(self):
        count = self.max
        index = randrange(0, len(self.text))

        if self.is_range:
            count = randrange(self.min, self.max)

        data = LoremIpsumGenerator._text[index].split(" ")

        while len(data) < count:
            index = index + 1
            try:
                more = LoremIpsumGenerator._text[index].split(" ")
                data.extend(more)
            except KeyError:
                more = LoremIpsumGenerator._text[index].split(" ")
                data.extend(more)

        return ' '.join(data[0:count])

    def action(self):
        return self.words()

