class MockingbirdGenerator(object):
    
    def __call__(self):
        return self.repo.action()
