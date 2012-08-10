import unittest
import context
from mockingbird import Mockingbird
from mockingbird.exceptions import MissingSpec


class MockingbirdExceptionsSuite(unittest.TestCase):

    def setUp(self):
        self.mockingbird = Mockingbird()

    def test_missing_spec_attr(self):
        mockingbird = self.mockingbird

        with self.assertRaises(MissingSpec):
            mockingbird.Phantom()

        with self.assertRaises(AttributeError):
            mockingbird.Phantom()

    def test_missing_spec_key(self):
        mockingbird = self.mockingbird

        with self.assertRaises(MissingSpec):
            mockingbird["Phantom"]

        with self.assertRaises(KeyError):
            mockingbird["Phantom"]