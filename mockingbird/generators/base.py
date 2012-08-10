class MockingbirdGenerator(object):

    def __call__(self, context):
        return self.repo.action(context)
