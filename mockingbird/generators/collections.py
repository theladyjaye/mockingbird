from .base import MockingbirdGenerator
from mockingbird.repositories.collections.choices import BooleanGenerator
from mockingbird.repositories.collections.choices import ChoiceGenerator
from mockingbird.repositories.collections.objects import ObjectGenerator
from mockingbird.repositories.collections.lists import ObjectListGenerator

class MockBoolean(MockingbirdGenerator):
    def __init__(self, value=None, repo=BooleanGenerator):
        self.repo = repo(value=value)

class MockChoice(MockingbirdGenerator):
    def __init__(self, choices, repo=ChoiceGenerator):
        self.repo = repo(choices=choices)

class MockObject(MockingbirdGenerator):
    def __init__(self, cls, repo=ObjectGenerator):
        self.repo = repo(cls)

class MockObjectList(MockingbirdGenerator):
    def __init__(self, cls, min=0, max=1, repo=ObjectListGenerator):
        self.repo = repo(cls, min=min, max=max)