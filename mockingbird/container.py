class MockBuilder(object):
    
    def __init__(self, cls, attrs):
        self.cls = cls
        self.attrs = attrs

    def __call__(self):
        obj = self.cls()
        for k,v in self.attrs.iteritems():
            setattr(obj, k, v())
        
        return obj

class Mockingbird(dict):

    def spec(self, cls, attrs):
        key = cls.__name__.lower()
        self[key] = MockBuilder(cls, attrs)

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key.lower())
        except KeyError:
            raise KeyError(key)

    def __getattr__(self, key):
        try:
             return dict.__getitem__(self, key.lower())
        except KeyError:
            raise AttributeError(key)