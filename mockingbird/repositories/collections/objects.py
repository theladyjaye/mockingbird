# from mockingbird import mockingbird

class ObjectGenerator(object):

    def __init__(self, cls):
        self.cls = cls.__name__

    # def action(self):
    #     try:
    #         return getattr(mockingbird, self.cls)
    #     except AttributeError:
    #         pass