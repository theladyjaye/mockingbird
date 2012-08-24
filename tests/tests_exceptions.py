import sys, os
sys.path.insert(0, os.path.abspath('..'))

import unittest
from mockingbird import Mockingbird
from mockingbird.exceptions import MissingSpec


class MockingbirdExceptionsSuite(unittest.TestCase):

    def setUp(self):
        self.mockingbird = Mockingbird()

    def test_missing_spec_attr(self):
        mockingbird = self.mockingbird

        self.assertRaises(MissingSpec, getattr, mockingbird, 'Phantom')
        self.assertRaises(AttributeError, getattr, mockingbird, 'Phantom')

    def test_missing_spec_key(self):
        mockingbird = self.mockingbird

        self.assertRaises(MissingSpec, mockingbird.get('Phantom'))
        self.assertRaises(KeyError, mockingbird.get('Phantom'))

if __name__ == '__main__':
    unittest.main()
