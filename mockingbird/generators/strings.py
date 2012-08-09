from .base import MockingbirdGenerator
from mockingbird.repositories.strings import LoremIpsumGenerator

class MockString(MockingbirdGenerator):
    
    def __init__(self, max=50, min=None, source=LoremIpsumGenerator):
        self.max = max
        self.min = min
        self.source = source()

    def __call__(self):
        return "foo"
