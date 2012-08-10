from .base import MockingbirdGenerator
from mockingbird.repositories.numbers.ints import IntGenerator

class MockInt(MockingbirdGenerator):
    def __init__(self, min=1, max=2, repo=IntGenerator):
        self.repo = repo(min,max)