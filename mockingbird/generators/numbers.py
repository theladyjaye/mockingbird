from .base import MockingbirdGenerator
from mockingbird.repositories.numbers.ints import IntGenerator

class MockInt(MockingbirdGenerator):
    def __init__(self, min=1, max=1, value=None, repo=IntGenerator):
        self.repo = repo(min, max, value)