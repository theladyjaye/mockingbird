class ObjectGenerator(object):

    def __init__(self, cls):
        self.cls = cls.__name__

    def action(self, context):
        try:
            return getattr(context, self.cls)()
        except AttributeError:
            pass
