from .base import MockingbirdGenerator
from mockingbird.repositories.collections.choices import BooleanGenerator
from mockingbird.repositories.collections.choices import ChoiceGenerator

class MockBoolean(MockingbirdGenerator):
    def __init__(self, value=None repo=BooleanGenerator):
        self.repo = repo(value=value)

class MockChoice(MockingbirdGenerator):
    def __init__(self, choices, repo=ChoiceGenerator):
        self.repo = repo(choices=choices)