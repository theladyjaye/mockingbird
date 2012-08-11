from .exceptions import MissingSpec


class MockBuilder(object):

    def __init__(self, cls, attrs, context):
        self.cls = cls
        self.attrs = attrs
        self.context = context

    def __call__(self):
        obj = self.cls()
        context = self.context
        for k, v in self.attrs.items():
            setattr(obj, k, v(context=context))

        return obj


class Mockingbird(dict):
    # descriptor to get current for instance?

    def spec(self, cls, attrs):
        key = cls.__name__.lower()
        self[key] = MockBuilder(cls, attrs, self)

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key.lower())
        except KeyError:
            raise MissingSpec(key)

    def __getattr__(self, key):
        try:
            return dict.__getitem__(self, key.lower())
        except KeyError:
            raise MissingSpec(key)
