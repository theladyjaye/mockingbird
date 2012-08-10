import pkg_resources
from random import randrange


class NameGenerator(object):
    _names = None

    @property
    def names(self):
        if not NameGenerator._names:
            data = pkg_resources.resource_stream("mockingbird.resources",
                                                 "names.txt")
            NameGenerator._names = []

            for line in data:
                NameGenerator._names.append(line.strip())

        return NameGenerator._names

    def action(self):
        names = self.names
        name_index = randrange(0, len(names))
        return names[name_index]
