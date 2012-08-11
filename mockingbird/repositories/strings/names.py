import pkg_resources
from random import randrange


class NameGenerator(object):
    _names = None

    @property
    def names(self):
        if not NameGenerator._names:
            NameGenerator._names = []

            with pkg_resources.resource_stream("mockingbird.resources",
                                                 "names.txt") as data:
                for line in data:
                    NameGenerator._names.append(line.strip())

        return NameGenerator._names

    def action(self, context):
        names = self.names
        name_index = randrange(0, len(names))
        return names[name_index]
