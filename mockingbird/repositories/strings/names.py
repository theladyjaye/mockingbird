import pkg_resources
from random import randrange


class NameGenerator(object):
    _names_first = None
    _names_last = None

    @property
    def names_first(self):
        if not NameGenerator._names_first:
            NameGenerator._names_first = []

            with pkg_resources.resource_stream("mockingbird.resources",
                                                 "names_first.txt") as data:
                for line in data:
                    NameGenerator._names_first.append(line.strip())

        return NameGenerator._names_first

    @property
    def names_last(self):
        if not NameGenerator._names_last:
            NameGenerator._names_last = []

            with pkg_resources.resource_stream("mockingbird.resources",
                                                 "names_last.txt") as data:
                for line in data:
                    NameGenerator._names_last.append(line.strip())

        return NameGenerator._names_last

    def action(self, context):
        first = self.names_first
        last = self.names_last
        first_index = randrange(0, len(first))
        last_index = randrange(0, len(last))
        return "%s %s" % (first[first_index], last[last_index])


class FirstNameGenerator(NameGenerator):

    def action(self, context):
        names = self.names_first
        name_index = randrange(0, len(names))
        return names[name_index]


class LastNameGenerator(NameGenerator):

    def action(self, context):
        names = self.names_last
        name_index = randrange(0, len(names))
        return names[name_index]


class UserNameGenerator(object):
    _words = None

    @property
    def words(self):
        if not UserNameGenerator._words:
            UserNameGenerator._words = []

            with pkg_resources.resource_stream("mockingbird.resources",
                                                 "words.txt") as data:
                for line in data:
                    UserNameGenerator._words.append(line.strip())

        return UserNameGenerator._words

    def action(self, context):
        words = self.words
        index1 = randrange(0, len(words))
        index2 = index1
        username = None
        has_number = bool(randrange(0, 2))

        while index2 == index1:
            index2 = randrange(0, len(words))

        if has_number:
            number = randrange(0, 100)
            username = "%s%s%i" % (words[index1], words[index2], number)
        else:
            username = "%s%s" % (words[index1], words[index2])

        return username
